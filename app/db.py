import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") or (
    f"postgresql://{os.getenv('todo_user')}:{os.getenv('todo_pass')}"
    f"@{os.getenv('POSTGRES_HOST', 'db')}:{os.getenv('POSTGRES_PORT', 5432)}/{os.getenv('todo_db')}"
)


for attempt in range(10):
    try:
        engine = create_engine(DATABASE_URL, echo=False, future=True)
        # Test connection
        connection = engine.connect()
        connection.close()
        print("Database connected!")
        break
    except psycopg2.OperationalError:
        print(f"Database not ready, waiting 3 seconds... (Attempt {attempt+1}/10)")
        time.sleep(3)
else:
    raise Exception("Database connection failed after several attempts")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
