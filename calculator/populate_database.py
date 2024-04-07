import mysql.connector

# Estabelece a conexão com o servidor MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  # Substitua "sua_senha" pela senha do seu MySQL
)

# Criação do cursor
cursor = connection.cursor()

try:
    # Criação do banco de dados
    cursor.execute("CREATE DATABASE IF NOT EXISTS calculadora_consumo")

    # Seleciona o banco de dados recém-criado
    cursor.execute("USE calculadora_consumo")

    # Criação da tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            documento VARCHAR(14) UNIQUE,
            cidade VARCHAR(255),
            estado VARCHAR(255),
            consumo INT,
            tipo VARCHAR(255),
            cobertura INT,
            tarifa FLOAT
        )
    """)

    # Inserção de dados na tabela
    cursor.executemany("""
        INSERT INTO cliente (nome, documento, cidade, estado, consumo, tipo, cobertura, tarifa)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, [
        ('Fischer, Livingston and Smith', '16460304009', 'Belo Horizonte', 'Minas Gerais', 407, 'Residencial', 90, 1.12307169),
        ('Tapia, Patel and Richardson', '62055616000117', 'Fortaleza', 'Ceará', 9667, 'Comercial', 90, 1.04820025),
        ('Solomon-Molina', '48471910055', 'Rio de Janeiro', 'Rio de Janeiro', 10046, 'Residencial', 95, 1.12307169),
        ('Harmon-Woodard', '75643674000103', 'Porto Alegre', 'Rio Grande do Sul', 1186, 'Industrial', 90, 0.95871974),
        ('Frye, Jones and Edwards', '23369997000157', 'Goiânia', 'Goiás', 16633, 'Comercial', 95, 1.04820025),
        ('Stone, Alvarez and Ford', '30800134000158', 'João Pessoa', 'Paraíba', 7032, 'Comercial', 90, 1.04820025),
        ('Higgins-Benson', '58716104000187', 'Vitória', 'Espírito Santo', 6146, 'Industrial', 90, 0.95871974),
        ('Reyes Group', '39522411000182', 'São Luís', 'Maranhão', 13012, 'Industrial', 95, 0.95871974),
        ('Meyer-Bowen', '38728930096', 'Campo Grande', 'Mato Grosso do Sul', 35440, 'Residencial', 99, 1.12307169),
        ('Hill, Garcia and Orozco', '14177992000131', 'São Paulo', 'São Paulo', 410, 'Industrial', 90, 0.95871974)
    ])

    # Confirma as alterações
    connection.commit()

except mysql.connector.Error as err:
    print("Erro ao executar a consulta:", err)

finally:
    # Fecha o cursor e a conexão
    cursor.close()
    connection.close()