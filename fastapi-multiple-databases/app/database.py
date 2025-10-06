
# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Defaults: two local SQLite files so nothing external is required.
DB1_URL = os.getenv("DATABASE1_URL", "sqlite:///./data/db1.sqlite3")
DB2_URL = os.getenv("DATABASE2_URL", "sqlite:///./data/db2.sqlite3")

# SQLite requires a special connect arg to allow connections across threads
connect_args_db1 = {"check_same_thread": False} if DB1_URL.startswith("sqlite") else {}
connect_args_db2 = {"check_same_thread": False} if DB2_URL.startswith("sqlite") else {}

engine_db1 = create_engine(DB1_URL, connect_args=connect_args_db1, future=True)
engine_db2 = create_engine(DB2_URL, connect_args=connect_args_db2, future=True)

SessionLocalDB1 = sessionmaker(bind=engine_db1, autoflush=False, autocommit=False)
SessionLocalDB2 = sessionmaker(bind=engine_db2, autoflush=False, autocommit=False)

BaseDB1 = declarative_base()
BaseDB2 = declarative_base()

def init_db():
    # import models so they are registered on the respective Base
    import app.models_db1  # noqa: F401
    import app.models_db2  # noqa: F401
    BaseDB1.metadata.create_all(bind=engine_db1)
    BaseDB2.metadata.create_all(bind=engine_db2)
