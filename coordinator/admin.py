from django.contrib import admin

from coordinator.models import Game, GameAdmin, Player, PlayerAdmin, GameLog, GameLogAdmin

# Register your models here.
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GameLog, GameLogAdmin)
