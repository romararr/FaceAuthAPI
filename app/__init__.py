from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

app = Flask(__name__)
app.config.from_object(Config)

# config database connection
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# seeders
seeder = FlaskSeeder()
seeder.init_app(app, db)

from app.models import order, orderStuff, user
from app import routes