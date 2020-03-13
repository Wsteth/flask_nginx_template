from flask import Flask
from core.config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='../static')
app.config.from_object(Config)
db = SQLAlchemy(app)

import core.routes
import api.users