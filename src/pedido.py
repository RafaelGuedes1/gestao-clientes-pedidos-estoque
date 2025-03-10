# filepath: meu-projeto-python/src/pedido.py
from database import create_connection
import mysql.connector

def create_pedido_table():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Pedido (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    cliente_id INT,
                    data_pedido DATE,
                    FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
                )
            """)
            connection.commit()
            print("Tabela Pedido criada com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar a tabela Pedido: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

def add_pedido(cliente_id, data_pedido):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO Pedido (cliente_id, data_pedido) VALUES (%s, %s)", (cliente_id, data_pedido))
            connection.commit()
            print("Pedido adicionado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar pedido: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

if __name__ == "__main__":
    create_pedido_table()
    add_pedido(1, "2025-03-10")