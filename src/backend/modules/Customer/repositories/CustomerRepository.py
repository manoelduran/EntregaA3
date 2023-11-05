import sqlite3
from modules.Customer.models.Customer import Customer
from infrastructure.database.sqliteDatabase import SqliteDatabase


class CustomerRepository:
    def __init__(self, database: SqliteDatabase):
        self.database = database

    def find_all(self):
        query = "SELECT * FROM customers"
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query)
                rows = cursor.fetchall()
                customers = [Customer(id=row[0], name=row[1], email=row[2],
                                      password=row[3], created_at=row[4]) for row in rows]
                return customers
        except sqlite3.Error as error:
            print(f"Error fetching customers: {error}")

    def find_one(self, id: int):
        query = "SELECT * FROM customers WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    customer = Customer(id=row[0], name=row[1], email=row[2],
                                        password=row[3], created_at=row[4])
                    return customer
                else:
                    print(f"Customer with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error fetching customer with ID {id}: {error}")

    def find_by_email(self, email: str):
        query = "SELECT * FROM customers WHERE email = ?"
        parameters = (email,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    customer = Customer(id=row[0], name=row[1], email=row[2],
                                        password=row[3], created_at=row[4])
                    return customer
                else:
                    print(f"Customer with email {email} not found.")
        except sqlite3.Error as error:
            print(f"Error fetching customer with email {email}: {error}")

    def create(self, customer: Customer):
        query = "INSERT INTO customers (name, email, password) VALUES (?, ?, ?)"
        parameters = (customer.name, customer.email, customer.password)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(
                    query, parameters)
                self.database.connection.commit()
            if cursor.rowcount > 0:
                return customer
            else:
                print(f"Customer with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error creating customer: {error}")

    def update(self, id: int, customer: Customer):
        query = "UPDATE customers SET name=?, email=?, password=? WHERE id=?"
        parameters = (customer.name, customer.email, customer.password, id)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                self.database.connection.commit()
                if cursor.rowcount > 0:
                    return customer
                else:
                    return print(f"Customer with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error updating customer with ID {id}: {error}")

    def delete(self, id: int):
        query = "DELETE FROM customers WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                customer = self.find_one(id)
                cursor = self.database.connection.execute(query, parameters)
                self.database.connection.commit()
                if cursor.rowcount > 0:
                    return customer
                else:
                    print(f"Customer with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error deleting customer with ID {id}: {error}")
