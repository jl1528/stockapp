import database

def create_db():
    return database.Base.metadata.create_all(bind = database.engine)

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

