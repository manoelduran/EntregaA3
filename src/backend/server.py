from infrastructure.database.schema import tablesSchema
from infrastructure.database.sqliteDatabase import SqliteDatabase
from main import app




def get_db():
    db = SqliteDatabase("my_database.db")
    db.connect()
    db.createTables(schema=tablesSchema)
    yield db
    db.disconnect()

def bootstrap():
    get_db()
    app()