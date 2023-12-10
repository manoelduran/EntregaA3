import sqlite3
from modules.Order.dtos.UpdateOrderDto import UpdateOrderDto
from modules.Order.dtos.CreateOrderDto import CreateOrderDto
from modules.Order.models.Order import Order
from infrastructure.database.sqliteDatabase import SqliteDatabase


class OrderRepository:
    def __init__(self, database: SqliteDatabase):
        self.database = database

    def find_all(self):
        query = "SELECT * FROM orders"
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query)
                rows = cursor.fetchall()

                orders = [Order(id=row[0], customer_id=row[1], payment_method=row[2],
                                product_id=row[3], quantity=row[4], ordered_at=row[5]) for row in rows]
                return orders
        except sqlite3.Error as error:
            print(f"Error fetching orders: {error}")

    def find_one(self, id: int):
        query = "SELECT * FROM orders WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                row = cursor.fetchone()
                if row:
                    order = Order(id=row[0], customer_id=row[1], payment_method=row[2],
                                  product_id=row[3], quantity=row[4], ordered_at=row[5])

                    return order
                else:
                    print(f"Order with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error fetching order with ID {id}: {error}")

    def find_all_by_customer_id(self, customer_id: int):

        query = "SELECT * FROM orders WHERE customer_id = ?"
        parameters = (customer_id,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                rows = cursor.fetchall()
                if rows:
                    orders = [Order(id=row[0], customer_id=row[1], payment_method=row[2],
                                    product_id=row[3], quantity=row[4], ordered_at=row[5]) for row in rows]

                    return orders
                else:
                    print(f"Orders with customer_id {customer_id} not found.")
        except sqlite3.Error as error:
            print(
                f"Error fetching orders with customer_id {customer_id}: {error}")

    def find_all_by_product_id(self, product_id: int):
        query = "SELECT * FROM orders WHERE product_id = ?"
        parameters = (product_id,)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                rows = cursor.fetchall()
                if rows:
                    orders = [Order(id=row[0], customer_id=row[1], payment_method=row[2],
                                    product_id=row[3], quantity=row[4], ordered_at=row[5]) for row in rows]
                    return orders
                else:
                    print(f"Orders with product_id {product_id} not found.")
        except sqlite3.Error as error:
            print(
                f"Error fetching orders with product_id {product_id}: {error}")

    def find_all_with_project(self):
        query = "SELECT * FROM orders"
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query)
                rows = cursor.fetchall()
                if rows:
                    orders = [Order(id=row[0], customer_id=row[1], payment_method=row[2],
                                    product_id=row[3], quantity=row[4], ordered_at=row[5]) for row in rows]
                    return orders
                else:
                    print(f"Orders not found.")
        except sqlite3.Error as error:
            print(
                f"Error fetching orders: {error}")

    def create(self, order: CreateOrderDto):
        query = "INSERT INTO orders (customer_id, payment_method, product_id, quantity) VALUES (?, ?, ?, ?)"
        parameters = (order.customer_id, order.payment_method,
                      order.product_id, order.quantity)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(
                    query, parameters)
                self.database.connection.commit()
            if cursor.rowcount > 0:
                return order
            else:
                print(f"Order with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error creating order: {error}")

    def update(self, id: int, order: UpdateOrderDto):
        query = "UPDATE orders SET customer_id=?, payment_method=?, product_id=?, quantity=? WHERE id=?"
        parameters = (order.customer_id, order.payment_method,
                      order.product_id, order.quantity, id)
        try:
            with self.database.connection:
                cursor = self.database.connection.execute(query, parameters)
                self.database.connection.commit()
                if cursor.rowcount > 0:

                    return order
                else:
                    return print(f"Order with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error updating order with ID {id}: {error}")

    def delete(self, id: int):
        query = "DELETE FROM orders WHERE id = ?"
        parameters = (id,)
        try:
            with self.database.connection:
                order = self.find_one(id)
                cursor = self.database.connection.execute(query, parameters)
                self.database.connection.commit()
                if cursor.rowcount > 0:
                    return order
                else:
                    print(f"Order with ID {id} not found.")
        except sqlite3.Error as error:
            print(f"Error deleting order with ID {id}: {error}")
