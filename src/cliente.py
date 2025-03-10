from database import create_connection
import mysql.connector

def create_cliente_table():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Cliente (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL
                )
            """)
            connection.commit()
            print("Tabela Cliente criada com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao criar a tabela Cliente: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

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

def add_cliente(nome, email):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO Cliente (nome, email) VALUES (%s, %s)", (nome, email))
            connection.commit()
            print("Cliente adicionado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar cliente: {err}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Falha na conexão com o banco de dados.")

if __name__ == "__main__":
    create_cliente_table()
    create_pedido_table()
    add_cliente("João Silva", "joao.silva@example.com")