from backend.settings import *

# This settings are for dev version of a local poker server
# Note that setting on an actual server used for assignments might (and will) be different

GRPC_SERVER_ADDRPORT = '[::]:50051'
GRPC_MAX_WORKERS = 64 # Note that each player reserves one worker, if this setting is low tournament may not be even able to start
GRPC_USE_RELOADER = True

GENERATE_TEST_PLAYERS = 4
GENERATE_BOT_PLAYERS = 16

CARD_GENERATED_IMAGE_SIZE = 32
CARD_GENERATED_IMAGE_NOISE_LEVEL = 0.15    # to change on the production server
CARD_GENERATED_IMAGE_ROTATE_MAX_ANGLE = 15 # to change on the production server

COORDINATOR_REVEAL_CARDS = False

COORDINATOR_TOURNAMENT_GRACE_PERIOD = 0.5 # sec

# This settings control for how long GRPC service should wait for a coordinator to be ready
# Normally if coordinator does not send ready event then something wrong is going on on server side
# We do not expect to hit this timeout setting, so we set it larger than the others
COORDINATOR_READY_TIMEOUT = 3600 # 1 hour

# Normally `KuhnCoordinator` needs to register each coordinator in a global dictionary
# We do not expect to hit this timeout setting, so we set it larger than the others
COORDINATOR_REGISTERED_TIMEOUT = 100 # 100 sec

# This option configures timeout for an agent to make an action
COORDINATOR_WAITING_TIMEOUT = 5  # 5 sec

# This option configures timeout for the server to process individual messages from players
COORDINATOR_DELAY_PROCESSING = 0.1

# This option configures timeout for the server to process card identification from the players
COORDINATOR_CARD_DELAY_PROCESSING = 1.0

# This option configures timeout for a waiting room connection
COORDINATOR_CONNECTION_TIMEOUT = 100  # 100 sec

# This is a secret password to create tournaments, to change on the production server
COORDINATOR_TOURNAMENTS_SECRET = 'qwerty'

COORDINATOR_REMOVE_CLOSED_COORDINATORS_INTERVAL = 10 # 10 sec

KUHN_GAME_INITIAL_BANK = 5
KUHN_ALLOW_BOTS = True
KUHN_BOT_FOLDER = 'bots'

BACKEND_GITHUB_URL = 'https://github.com/tue-5ARA0/poker-server-backend'
CLIENT_GITHUB_URL  = 'https://github.com/tue-5ARA0-2024-Q1/poker-server-client'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[{levelname}][{asctime}]: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filename': 'server.log',
            'formatter': 'default'
        }
    },
    'loggers': {
        'kuhn.coordinator': {
            'handlers': [ 'console', 'file' ],
            'level': 'DEBUG'
        },
        'kuhn.waiting': {
            'handlers': [ 'console', 'file' ],
            'level': 'DEBUG'
        },
        'kuhn.game': {
            'handlers': [ 'console', 'file' ],
            'level': 'DEBUG'
        },
        'service.coordinator': {
            'handlers': [ 'console', 'file' ],
            'level': 'DEBUG'
        }
    }
}
