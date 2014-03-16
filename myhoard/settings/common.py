# Flask
DEBUG = False
TESTING = False

# Auth
AUTH_KEEP_ALIVE_TIME = 300

# Image
MAX_CONTENT_LENGTH = 10 * 1024 * 1024 # 10MiB
IMAGE_EXTENSIONS = ('jpg', 'jpeg', 'png')
IMAGE_THUMBNAIL = (32, 32, True)  # w, h, fill_mode: true | scale_mode: false

# Custom error codes
ERROR_CODE_NO_INCOMING_FILE_DATA = 98
ERROR_CODE_NO_INCOMING_JSON_DATA = 99

ERROR_CODE_VALIDATION = 100
ERROR_CODE_DUPLICATE = 101

ERROR_CODE_AUTH = 102
ERROR_CODE_AUTH_NOT_PROVIDED = 103
ERROR_CODE_AUTH_BAD_PROVIDED = 104
ERROR_CODE_AUTH_FAILED = 105

ERROR_CODE_MEDIA_BAD_EXT = 106
ERROR_CODE_MEDIA_ALREADY_HAVE_PARENT = 107

ERROR_CODE_NOT_EXIST = 404

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'root': {
        'level': 'NOTSET',
        'handlers': ['console', 'file'],
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'filename': 'myHoard.log',
            'mode': 'a',
            'maxBytes': 2097152, #2MB
            'backupCount': 64,
        },
    },

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
}
