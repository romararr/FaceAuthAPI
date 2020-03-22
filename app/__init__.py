from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# config jwt
jwt = JWTManager(app)

# config database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# seeders
seeder = FlaskSeeder()
seeder.init_app(app, db)

from app.models import order, orderStuff, user
from app import routes