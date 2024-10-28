from sqlalchemy import create_engine, Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

# Define base
Base = declarative_base()

class LocatorData(Base):
    __tablename__ = "locator_data"
    original_locator = Column(String, primary_key=True)
    alternative_locator = Column(String)
    status = Column(String)
    heal = Column(Boolean, default=False)
    healed_timestamp = Column(DateTime)
    screenshot = Column(String)

# Database setup
engine = create_engine(config.DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
