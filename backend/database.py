from sqlmodel import SQLModel, create_engine, Session
from config import SUPABASE_PROJECT_URL

engine = create_engine(SUPABASE_PROJECT_URL, echo=False)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
