import sys
from sqlmodel import SQLModel, Session, create_engine, text
import os
from dotenv import load_dotenv
from sqlalchemy.exc import OperationalError


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def init_db():
    try:
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
        with Session(engine) as session:
            session.exec(text("SELECT 1"))
        print("✅ Connexion à PostgreSQL établie avec succès.")
    except OperationalError as e:
        print("❌ Impossible de se connecter à PostgreSQL.")
        print("Détail :", str(e))
        sys.exit(1)
