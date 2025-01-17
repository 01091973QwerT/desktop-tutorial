from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
from sqlalchemy import Column, Integer, String, Boolean


DATABASE_URL = 'sqlite:///taskmanager.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base:
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

    id = Column(Integer, primary_key=True, index=True)


Base = declarative_base(cls=Base)



