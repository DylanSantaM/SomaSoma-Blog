from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(db, app)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = "login"

from app import routes, models, errors
