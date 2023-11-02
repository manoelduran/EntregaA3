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
            self.connection.executescript(schema)
        except sqlite3.Error as error:
            print(f"Erro ao criar o esquema da tabela: {error}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(
                f"Conexão com o banco de dados '{self.name}' encerrada com sucesso.")
        else:
            print("Nenhuma conexão ativa.")
            
    def execute_query(self, query: str, parameters=None):
        try:
            if parameters:
                self.connection.execute(query, parameters)
            else:
                self.connection.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as error:
            print(f"Error executing query: {error}")
