from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.shared.settings.config import postgres_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://{postgres_db['username']}:{postgres_db['password']}@{postgres_db['host']}:{postgres_db['port']}/{postgres_db['db']}"
db = SQLAlchemy()
db.init_app(app)
ma = Marshmallow(app)
