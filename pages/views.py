
from django.shortcuts import render
from coordinator.models import Game, GameCoordinatorTypes, GameRound, Player, RoomRegistration, Tournament, TournamentRound, TournamentRoundBracketItem, TournamentRoundGame, WaitingRoom
from django.db.models import Count, Q, F, Case, When, IntegerField, Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponseRedirect
from django.conf import settings

from pages.forms import SearchGameForm, SearchTournamentForm
from pages.models import Announcement

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {
        'announcements': list(Announcement.objects.filter(is_hidden = False)),
        'backend_github_url': settings.BACKEND_GITHUB_URL,
        'client_github_url': settings.CLIENT_GITHUB_URL
    })

def games_view(request, *args, **kwargs):
    return render(request, "games.html", {
        'games': Game.objects.all().order_by('-created_at')[:50],
        'form': kwargs['form'] if 'form' in kwargs else SearchGameForm()
    })

def tournaments_view(request, *args, **kwargs):
    return render(request, "tournaments.html", {
        'tournaments': Tournament.objects.filter(coordinator__isnull = False).order_by('-created_at')[:50],
        'form': kwargs['form'] if 'form' in kwargs else SearchTournamentForm()
    })

def game_search_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SearchGameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            id = form.cleaned_data['game_or_coordinator_id']
            return HttpResponseRedirect(f'/game/{ id }/')
        return games_view(request, form = form)
    return HttpResponseRedirect("/games/")

def tournament_search_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SearchTournamentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            id = form.cleaned_data['tournament_or_coordinator_id']
            return HttpResponseRedirect(f'/tournament/{ id }/')
        return tournaments_view(request, form = form)
    return HttpResponseRedirect("/tournaments/")
    

def game_view(request, *args, **kwargs):
    id = kwargs['game_id']

    try:
        context = {}

        game  = None
        games_by_id  = Game.objects.filter(id = id)
        games_by_cid = Game.objects.filter(created_by__id = id)

        if len(games_by_id) != 0:
            game = games_by_id[0]
        elif len(games_by_cid) != 0:
            game = games_by_cid[0]

        if game == None:
            raise ValueError() 

        context['is_game_found'] = True
        context['game']          = game
        context['rounds']        = list(GameRound.objects.filter(game__id = game.id))[:-1]

        return render(request, "game.html", context)
    except Exception as e:
        return render(request, "game.html", { 'is_game_found': False })

def fetch_leaderboard_data():
    players_data = Player.objects.annotate(
        games_total=Count('player1_games', distinct=True) + Count('player2_games', distinct=True),
        games_won=Count('games_won', distinct=True),
        games_lost=F('games_total') - F('games_won'),
        tournaments_participated=Count(
            'roomregistration__room__coordinator',
            filter=Q(
                roomregistration__room__coordinator__coordinator_type__in=[
                    GameCoordinatorTypes.TOURNAMENT_PLAYERS,
                    GameCoordinatorTypes.TOURNAMENT_PLAYERS_WITH_BOTS
                ]
            ),
            distinct=True
        ),
        tournaments_won=Count('tournaments_won', distinct=True)
    ).values('name', 'group', 'games_total', 'games_won', 'games_lost', 'tournaments_participated', 'tournaments_won', 'is_bot')

    players = []
    bots = []

    for player in players_data:
        stats = {
            'name': player['name'],
            'group': player['group'],
            'games_total': player['games_total'],
            'games_won': player['games_won'],
            'games_lost': player['games_lost'],
            'tournaments_participated': player['tournaments_participated'],
            'tournaments_won': player['tournaments_won']
        }
        if not player['is_bot']:
            players.append(stats)
        else:
            bots.append(stats)

    # Aggregate bot stats
    aggr_bots_stats = Player.objects.filter(is_bot=True).aggregate(
        games_total=Coalesce(Sum('player1_games', distinct=True), 0) + Coalesce(Sum('player2_games', distinct=True), 0),
        games_won=Coalesce(Sum('games_won'), 0),
        tournaments_participated=Coalesce(Sum(
            Case(
                When(
                    roomregistration__room__coordinator__coordinator_type__in=[
                        GameCoordinatorTypes.TOURNAMENT_PLAYERS,
                        GameCoordinatorTypes.TOURNAMENT_PLAYERS_WITH_BOTS
                    ],
                    then=1
                ),
                default=0,
                output_field=IntegerField()
            )
        ), 0),
        tournaments_won=Coalesce(Sum('tournaments_won'), 0)
    )

    aggr_bots_stats['name'] = 'Bots (in total)'
    aggr_bots_stats['games_lost'] = aggr_bots_stats['games_total'] - aggr_bots_stats['games_won']

    leaderboard = [*players, aggr_bots_stats]
    leaderboard = sorted(leaderboard, key=lambda d: -d['tournaments_won'])

    return leaderboard

def leaderboard_view(request, *args, **kwargs):
    leaderboard = fetch_leaderboard_data()
    return render(request, "leaderboard.html", {'leaderboard': leaderboard})

def tournament_view(request, *args, **kwargs):
    try: 
        id = kwargs['tournament_id']

        tournament  = None
        tournaments_by_id  = Tournament.objects.filter(id = id)
        tournaments_by_cid = Tournament.objects.filter(coordinator__id = id)
        
        if len(tournaments_by_id) != 0:
            tournament = tournaments_by_id[0]
        elif len(tournaments_by_cid) != 0:
            tournament = tournaments_by_cid[0]

        if tournament == None:
            raise ValueError()            

        waiting_room  = WaitingRoom.objects.get(coordinator__id = tournament.coordinator.id)
        registrations = RoomRegistration.objects.filter(room__id = waiting_room.id)

        rounds = sorted(list(TournamentRound.objects.filter(tournament__id = tournament.id)), key = lambda d: d.index)

        def fetch_rounds_data(round):
            bracket_items = sorted(list(TournamentRoundBracketItem.objects.filter(round__id = round.id)), key = lambda d: d.position)
            games         = list(map(lambda bracket_item: next(iter(list(TournamentRoundGame.objects.filter(bracket_item__id = bracket_item.id))), None), bracket_items))
            brackets      = list(map(lambda tuple: { 'bracket_item': tuple[0], 'game': tuple[1] }, zip(bracket_items, games)))
            return { 'round': round, 'brackets': brackets }

        rounds_data = [] 
        try:
            for round in rounds:
                rounds_data.append(fetch_rounds_data(round))
        except Exception:
            pass



        return render(request, "tournament.html", {
            'tournament_found': True,
            'tournament': tournament,
            'rounds': rounds_data,
            'registrations': registrations
        })
    except Exception as e:
        return render(request, "tournament.html", { 'tournament_found': False })