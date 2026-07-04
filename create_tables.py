from app.core.database import Base
from app.core.database import engine

from app.models.person import Person

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Done.")
