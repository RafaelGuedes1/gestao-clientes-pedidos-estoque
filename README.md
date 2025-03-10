# Projeto de Gestão de Clientes, Pedidos e Estoque

## Descrição
Este projeto é um sistema de gestão de clientes, pedidos e estoque desenvolvido em Python com integração ao banco de dados MySQL. O sistema permite cadastrar, consultar, deletar e modificar clientes, adicionar produtos ao estoque e registrar pedidos.

## Estrutura do Projeto


meu-projeto-python ├── src │ ├── init.py │ ├── cliente.py │ ├── pedido.py │ ├── estoque.py │ ├── database.py │ ├── main.py │ └── requirements.txt └── .env



## Configuração

### Pré-requisitos
- Python 3.x
- MySQL
- Biblioteca `mysql-connector-python`
- Biblioteca `python-dotenv`

### Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/RafaelGuedes1/gestao-clientes-pedidos-estoque.git
    cd gestao-clientes-pedidos-estoque
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Linux/Mac
    ```

3. Instale as dependências:
    ```sh
    pip install -r src/requirements.txt
    ```

4. Configure as variáveis de ambiente no arquivo `.env`:
    ```plaintext
    DB_HOST=localhost
    DB_USER=seu_usuario
    DB_PASSWORD=sua_senha
    DB_NAME=nome_do_banco
    ```

## Uso
1. Execute o script `main.py` para iniciar o sistema:
    ```sh
    python src/main.py
    ```

2. Siga as instruções no menu para gerenciar clientes, pedidos e estoque.

### Menu Principal
- `1. Clientes`: Abre o menu de gestão de clientes.
- `2. Estoque`: Abre o menu de gestão de estoque.
- `3. Pedidos`: Abre o menu de gestão de pedidos.
- `4. Sair`: Encerra o sistema.

### Menu Clientes
- `1. Cadastrar Cliente`: Permite cadastrar um novo cliente.
- `2. Consultar Cliente`: (Em desenvolvimento) Permite consultar um cliente.
- `3. Deletar Cliente`: (Em desenvolvimento) Permite deletar um cliente.
- `4. Modificar Cliente`: (Em desenvolvimento) Permite modificar um cliente.
- `5. Voltar`: Retorna ao menu principal.

### Menu Estoque
- `1. Adicionar Produto`: Permite adicionar um novo produto ao estoque.
- `2. Consultar Estoque`: (Em desenvolvimento) Permite consultar o estoque.
- `3. Voltar`: Retorna ao menu principal.

### Menu Pedidos
- `1. Adicionar Pedido`: Permite registrar um novo pedido.
- `2. Consultar Pedidos`: (Em desenvolvimento) Permite consultar pedidos.
- `3. Voltar`: Retorna ao menu principal.

## Estrutura dos Arquivos

### `cliente.py`
Contém funções para criar a tabela `Cliente` e adicionar clientes.

### `pedido.py`
Contém funções para criar a tabela `Pedido` e adicionar pedidos.

### `estoque.py`
Contém funções para criar a tabela `Estoque` e adicionar produtos ao estoque.

### `database.py`
Configura a conexão com o banco de dados MySQL usando variáveis de ambiente.

### `main.py`
Contém o menu principal e submenus para gerenciar clientes, pedidos e estoque.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
