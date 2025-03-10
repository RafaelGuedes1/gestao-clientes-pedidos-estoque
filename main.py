from cliente import create_cliente_table, add_cliente
from pedido import create_pedido_table, add_pedido
from estoque import create_estoque_table, add_produto

def menu_clientes():
    while True:
        print("\nMenu Clientes:")
        print("1. Cadastrar Cliente")
        print("2. Consultar Cliente")
        print("3. Deletar Cliente")
        print("4. Modificar Cliente")
        print("5. Voltar")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")
            add_cliente(nome, email)
        elif escolha == '2':
            # Função para consultar cliente
            pass
        elif escolha == '3':
            # Função para deletar cliente
            pass
        elif escolha == '4':
            # Função para modificar cliente
            pass
        elif escolha == '5':
            break
        else:
            print("Escolha inválida. Tente novamente.")

def menu_estoque():
    while True:
        print("\nMenu Estoque:")
        print("1. Adicionar Produto")
        print("2. Consultar Estoque")
        print("3. Voltar")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            produto = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            add_produto(produto, quantidade)
        elif escolha == '2':
            # Função para consultar estoque
            pass
        elif escolha == '3':
            break
        else:
            print("Escolha inválida. Tente novamente.")

def menu_pedidos():
    while True:
        print("\nMenu Pedidos:")
        print("1. Adicionar Pedido")
        print("2. Consultar Pedidos")
        print("3. Voltar")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            cliente_id = int(input("Digite o ID do cliente: "))
            data_pedido = input("Digite a data do pedido (AAAA-MM-DD): ")
            add_pedido(cliente_id, data_pedido)
        elif escolha == '2':
            # Função para consultar pedidos
            pass
        elif escolha == '3':
            break
        else:
            print("Escolha inválida. Tente novamente.")

def main():
    # Criar tabelas
    create_cliente_table()
    create_pedido_table()
    create_estoque_table()

    while True:
        print("\nMenu Principal:")
        print("1. Clientes")
        print("2. Estoque")
        print("3. Pedidos")
        print("4. Sair")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            menu_clientes()
        elif escolha == '2':
            menu_estoque()
        elif escolha == '3':
            menu_pedidos()
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()