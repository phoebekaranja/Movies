from flask import Flask
# from .config import Devconfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    #creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)

    # Will add the views and forms
    return app
# # Initializing application
# app = Flask(__name__,instance_relative_config = True)
# #Setting up configuration
# app.config.from_object(Devconfig)
# app.config.from_pyfile('config.py')
# #Initializing Flask Extensions
# bootstrap= Bootstrap(app)
# from app import views
# from app import error