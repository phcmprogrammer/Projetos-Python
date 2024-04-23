import mysql.connector

# Função para conectar ao banco de dados
connect_to_db = lambda host, user, password, database: mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Função para executar uma consulta SQL
execute_query = lambda connection, query: connection.cursor().execute(query)

# Função para buscar todos os registros de uma tabela
fetch_all_records = lambda cursor: cursor.fetchall()

# Função para inserir um registro em uma tabela
insert_record = lambda connection, query: execute_query(connection, query)

# Função para remover um registro de uma tabela
remove_record = lambda connection, query: execute_query(connection, query)

# Função para consultar registros de uma tabela
select_records = lambda connection, query: fetch_all_records(execute_query(connection, query))

# Função principal
def main():
    # Conectando ao banco de dados
    connection = connect_to_db('host', 'root', 'password', 'database')

    # Inserindo um registro na tabela USERS
    insert_record(connection, "INSERT INTO USERS (id, name, country, id_console) VALUES (1, 'John', 'USA', 1)")

    # Removendo um registro da tabela VIDEOGAMES
    remove_record(connection, "DELETE FROM VIDEOGAMES WHERE id_console = 1")

    # Consultando todos os registros da tabela GAMES
    games = select_records(connection, "SELECT * FROM GAMES")

    # Exibindo os registros consultados
    for game in games:
        print(game)

    # Fechando a conexão com o banco de dados
    connection.close()

# Executando o programa
if __name__ == "__main__":
    main()
