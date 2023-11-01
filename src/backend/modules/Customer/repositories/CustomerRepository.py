from infrastructure.database.sqliteDatabase import SqliteDatabase


class CustomerRepository:
    def __init__(self, database: SqliteDatabase):
        self.database = database

    def find_all(self):
        print(self.database.name)

    def find_one(self, id: int):
        print(self.database.name)
