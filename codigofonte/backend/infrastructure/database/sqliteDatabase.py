import sqlite3


class SqliteDatabase:
    def __init__(self, name: str):
        self.name = name

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.name)
            print(
                f"Conexão com o banco de dados '{self.name}' estabelecida com sucesso.")
        except sqlite3.Error as error:
            print(f"Erro ao conectar ao banco de dados '{self.name}': {error}")

    def create_tables(self, schema: str):
        try:
            with sqlite3.connect(self.name) as connection:
                connection.executescript(schema)

                print("Tables created successfully.")
        except sqlite3.Error as error:
            print(f"Erro ao criar o esquema da tabela: {error}")

    def seed_data(self):
        try:
            with sqlite3.connect(self.name) as connection:
                cursor = connection.cursor()

                for i in range(1, 11):
                    cursor.execute("INSERT INTO customers (name, email, password) VALUES (?, ?, ?)",
                                   (f"Customer{i}", f"customer{i}@example.com", f"password{i}"))

                for i in range(1, 11):
                    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                                   (f"Product{i}", i * 10, 50))

                for i in range(1, 11):
                    cursor.execute("INSERT INTO orders (customer_id, payment_method, product_id, quantity) VALUES (?, ?, ?, ?)",
                                   (i, "Credit Card", i, 2))

            print("Seed data inserted successfully.")
        except sqlite3.Error as error:
            print(f"Error seeding data: {error}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(
                f"Conexão com o banco de dados '{self.name}' encerrada com sucesso.")
        else:
            print("Nenhuma conexão ativa.")

    def execute_query(self, query: str, parameters=None):
        try:
            with sqlite3.connect(self.name) as connection:
                cursor = self.connection.cursor()
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)
                connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as error:
            print(f"Error executing query: {error}")
