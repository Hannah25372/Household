import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from household_service.database.database import Base


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine)
    with TestingSession() as session:
        yield session
    Base.metadata.drop_all(engine)
    engine.dispose()