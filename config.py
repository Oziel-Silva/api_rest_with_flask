from flask import Blueprint, Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy


class ServerAPI():
    """
    Defines application server factory and configuration, database
    connection, namespace to be used and place for running as well.
    """

    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint,
                       doc='/doc',
                       title='API',
                       default_label='Generic_API',
                       default='Methods',
                       version='1.0.0'
                       )
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_ECHO'] = True
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

       
    def run(self):
        self.app.run(port=8000, debug=True, host='localhost')


db = SQLAlchemy()
ma = Marshmallow()
server = ServerAPI()

