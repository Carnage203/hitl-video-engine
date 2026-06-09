from sqlmodel import SQLModel, create_engine, Session
from config import SUPABASE_PROJECT_URL

engine = create_engine(SUPABASE_PROJECT_URL, echo=False, connect_args={"check_same_thread": False})

