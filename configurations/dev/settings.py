from backend.settings import *

# This settings are for dev version of a local poker server
# Note that setting on an actual server used for assignments might (and will) be different

GENERATE_TEST_PLAYERS = 2

CARD_GENERATED_IMAGE_SIZE = 32
CARD_GENERATED_IMAGE_NOISE_LEVEL = 0.15
CARD_GENERATED_IMAGE_ROTATE_MAX_ANGLE = 15

COORDINATOR_REVEAL_CARDS = False

# This settings control for how long GRPC service should wait for a coordinator to be ready
# Normally if coordinator does not send ready event then something wrong is going on on server side
# We do not expect to hit this timeout setting, so we set it larger than the others
COORDINATOR_READY_TIMEOUT = 100 # 100 sec

# Normally `KuhnCoordinator` needs to register each coordinator in a global dictionary
# We do not expect to hit this timeout setting, so we set it larger than the others
COORDINATOR_REGISTERED_TIMEOUT = 100 # 100 sec

# This option configures timeout for an agent to make an action
COORDINATOR_WAITING_TIMEOUT = 5  # 5 sec

# This option configures timeout for a waiting room connection
COORDINATOR_CONNECTION_TIMEOUT = 10  # 5 sec

KUHN_GAME_INITIAL_BANK = 5
KUHN_ALLOW_BOTS = True
KUHN_BOT_FOLDER = './bots'

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
