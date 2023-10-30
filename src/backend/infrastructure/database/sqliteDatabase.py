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

    def createTables(self, schema: str):
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
