from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./telegram_avatar_changer.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False, "timeout": 15}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(String, unique=True, nullable=False)
    api_hash = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    secret_tg_key = Column(String, nullable=True)


Base.metadata.create_all(bind=engine)
