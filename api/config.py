''' Arquivo de configuração '''

DEBUG = True
CSRF_ENABLED = True

DOMAIN_NAME = 'http://localhost'

UPLOAD_FOLDER = '/api/media'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

MONGO_URI = "mongodb://dbagrofloresta:dbagrofloresta@db_mongo:27017/dbagrofloresta"

# set log level as: DEBUG | INFO | ERROR
LOG_FILE = "API-OUTPUT.log"
LOG_LEVEL = 'DEBUG'
