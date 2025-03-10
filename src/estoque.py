# filepath: meu-projeto-python/src/estoque.py
from database import create_connection
import mysql.connector

def create_estoque_table():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Estoque (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    produto VARCHAR(255) NOT NULL,
                    quantidade INT NOT NULL
                )
            """)
            connection.commit()
            print("Tabela Estoque criada com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar a tabela Estoque: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

def add_produto(produto, quantidade):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO Estoque (produto, quantidade) VALUES (%s, %s)", (produto, quantidade))
            connection.commit()
            print("Produto adicionado ao estoque com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar produto ao estoque: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

if __name__ == "__main__":
    create_estoque_table()
    add_produto("Produto A", 100)