import sqlite3
from infrastructure.database.sqliteDatabase import SqliteDatabase

class CustomerRepository:
    def __init__(self, database: SqliteDatabase):
        self.database = database

    def find_all(self):
            query = "SELECT * FROM customers"
            try:
                cursor = self.database.connection.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print("ID:", row[0])
                    print("Nome:", row[1])
                    print("Email:", row[2])
                    print("Senha:", row[3])
                    print("Created At:", row[4])
            except sqlite3.Error as error:
                print(f"Error fetching all customers: {error}")
            print(self.database.name)

    def find_one(self, id: int):
            query = "SELECT * FROM customers WHERE id = ?"
            parameters = (id,)
            try:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    print("ID:", row[0])
                    print("Nome:", row[1])
                    print("Email:", row[2])
                    print("Senha:", row[3])
                    print("Created At:", row[4])
                else:
                    print(f"Customer with ID {id} not found.")
            except sqlite3.Error as error:
                print(f"Error fetching customer with ID {id}: {error}")
            print(self.database.name)
        
    def create(self):
        print(self.database.name)
        
    def update(self):
        print(self.database.name)

    def delete(self):
        print(self.database.name)
        

