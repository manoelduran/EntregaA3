import sqlite3
from modules.Product.dtos.CreateProductDto import CreateProductDto
from modules.Product.dtos.UpdateProductDto import UpdateProductDto
from modules.Product.models.Product import Product
from infrastructure.database.sqliteDatabase import SqliteDatabase


class ProductRepository:
    def __init__(self, database: SqliteDatabase):
        self.database = database

    def find_all(self):
        query = "SELECT * FROM products"
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query)
                rows = cursor.fetchall()
                products = [Product(id=row[0], name=row[1], price=row[2],
                                    quantity=row[3], created_at=row[4]) for row in rows]
                return products
        except sqlite3.Error as error:
            print(f"Error fetching products: {error}")

    def find_one(self, id: int):
        query = "SELECT * FROM products WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    product = Product(id=row[0], name=row[1], price=row[2],
                                      quantity=row[3], created_at=row[4])
                    return product
                else:
                    print(f"Product with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error fetching product with ID {id}: {error}")

    def find_by_name(self, name: str):
        query = "SELECT * FROM products WHERE name = ?"
        parameters = (name,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    product = Product(id=row[0], name=row[1], price=row[2],
                                      quantity=row[3], created_at=row[4])
                    return product
                else:
                    print(f"Product with name {name} not found.")
        except sqlite3.Error as error:
            print(f"Error fetching product with name {name}: {error}")

    def create(self, product: CreateProductDto):
        query = "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)"
        parameters = (product.name, product.price, product.quantity)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(
                    query, parameters)
                self.database.connection.commit()
            if cursor.rowcount > 0:
                return product
            else:
                print(f"Product not found.")
        except sqlite3.Error as error:
            print(f"Error creating product: {error}")

    def update(self, id: int, product: UpdateProductDto):
        query = "UPDATE products SET name=?, price=?, quantity=? WHERE id=?"
        parameters = (product.name, product.price, product.quantity, id)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)

                self.database.connection.commit()
                if cursor.rowcount > 0:
                    return product
                else:
                    return print(f"Product with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error updating product with ID {id}: {error}")

    def delete(self, id: int):
        query = "DELETE FROM products WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                product = self.find_one(id)
                cursor = self.database.connection.execute(query, parameters)
                self.database.connection.commit()
                if cursor.rowcount > 0:
                    return product
                else:
                    print(f"Product with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error deleting product with ID {id}: {error}")
