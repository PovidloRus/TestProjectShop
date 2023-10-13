from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from src.shared.settings.config import postgres_db

base = declarative_base()
engine = create_engine(
    f"postgresql+psycopg2://{postgres_db['username']}:{postgres_db['password']}@"
    f"{postgres_db['host']}:{postgres_db['port']}/{postgres_db['db']}",
    echo=True)
