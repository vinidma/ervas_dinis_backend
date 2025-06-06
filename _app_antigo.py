from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuração do Banco de Dados MySQL
# Lembre-se que você usou MYSQL_ROOT_PASSWORD=root no seu comando Docker
db_config = {
    'host': '127.0.0.1',  # Ou 'localhost'
    'user': 'root',
    'password': 'root',
    # 'database': 'ervasdinis' # Vamos criar o banco de dados primeiro
    'port': 3306 # Porta que você mapeou no Docker
}

# Função para conectar ao banco de dados e criar o banco/tabelas se não existirem
def init_db():
    try:
        # Conectar ao servidor MySQL (sem especificar o banco de dados inicialmente)
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            port=db_config['port']
        )
        cursor = conn.cursor()

        # Criar o banco de dados 'ervasdinis' se ele não existir
        cursor.execute("CREATE DATABASE IF NOT EXISTS ervasdinis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print("Banco de dados 'ervasdinis' verificado/criado.")
        cursor.execute("USE ervasdinis;") # Selecionar o banco de dados

        # Definir as tabelas (relembrando nossa modelagem)
        criar_tabela_categorias = """
        CREATE TABLE IF NOT EXISTS Categorias (
            id_categoria INT AUTO_INCREMENT PRIMARY KEY,
            nome_categoria VARCHAR(100) NOT NULL UNIQUE,
            descricao_categoria TEXT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """

        criar_tabela_ervas = """
        CREATE TABLE IF NOT EXISTS Ervas (
            id_erva INT AUTO_INCREMENT PRIMARY KEY,
            id_categoria INT,
            nome_popular_erva VARCHAR(150) NOT NULL,
            nome_cientifico_erva VARCHAR(150),
            descricao_erva TEXT,
            beneficios_erva TEXT,
            modo_uso_erva TEXT,
            caminho_imagem_erva VARCHAR(255),
            preco_erva DECIMAL(10, 2),
            estoque_erva INT,
            FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria) ON DELETE SET NULL ON UPDATE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        cursor.execute(criar_tabela_categorias)
        print("Tabela 'Categorias' verificada/criada.")
        cursor.execute(criar_tabela_ervas)
        print("Tabela 'Ervas' verificada/criada.")

        conn.commit() # Salvar as alterações

    except Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão com MySQL fechada após inicialização.")

# Rota de Teste
@app.route('/')
def home():
    return "Bem-vindo ao backend da Ervas Dinis!"

# Rota para testar a conexão com o banco (opcional)
@app.route('/test_db')
def test_db_connection():
    try:
        # Atualiza a configuração para incluir o banco de dados específico
        current_db_config = db_config.copy()
        current_db_config['database'] = 'ervasdinis'

        conn = mysql.connector.connect(**current_db_config)
        if conn.is_connected():
            db_Info = conn.get_server_info()
            conn.close()
            return jsonify(message="Conexão com MySQL bem-sucedida!", server_version=db_Info)
        else:
            return jsonify(message="Falha na conexão com MySQL.")
    except Error as e:
        return jsonify(message=f"Erro ao conectar com MySQL: {e}")

if __name__ == '__main__':
    init_db() # Chama a função para criar o banco e as tabelas ao iniciar a app
    app.run(debug=True, host='0.0.0.0', port=5000) # Flask rodará na porta 5000