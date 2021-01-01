import os
import logging

from flask import Flask
from flask_cors import CORS

import routes
import config

# inicia flask
app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

# configura logging
logging_level = getattr(logging, config.LOG_LEVEL.upper())
logging.basicConfig(filename=config.LOG_FILE,level=config.LOG_LEVEL)

# configura CORS(
CORS(app, resources={r"/*": { "origins": "*"}})

# inclui rotas e inicializa-as
routes.initialize_routes(app)

if __name__ == '__main__':
    if os.environ['ENV'] == 'prod' or os.environ['ENV'] == 'hmg':
        context = (os.environ['CERT'], os.environ['KEY'])
        app.run(debug=True, host=os.environ['HOST'],port=os.environ['PORT'],
                ssl_context=context)
    else:
        app.run(debug=True, host=os.environ['HOST'],port=os.environ['PORT'])
    logging.getLogger('flask_cors').level = logging.DEBUG
