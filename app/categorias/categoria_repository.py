# ervas_dinis_backend/app/categorias/categoria_repository.py

from mysql.connector import Error
from app.db_config.database import get_db_connection
from flask import current_app

class CategoriaRepository:

    def listar_todas(self):
        """Busca todas as categorias no banco de dados, ordenadas pelo nome."""
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:

                current_app.logger.error("Falha ao conectar ao banco de dados para listar categorias.")
                return []


            cursor = conn.cursor(dictionary=True)
            sql = "SELECT id_categoria, nome_categoria, descricao_categoria FROM Categorias ORDER BY nome_categoria ASC"
            cursor.execute(sql)
            categorias = cursor.fetchall()
            return categorias
        except Error as e:
            current_app.logger.error(f"Erro no repositório ao listar categorias: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def criar(self, nome_categoria, descricao_categoria=None):
        """Cria uma nova categoria no banco de dados."""
        conn = None
        cursor = None
        try:
            conn = get_db_connection()
            if conn is None:
                current_app.logger.error("Falha ao conectar ao banco de dados para criar categoria.")
                return None

            cursor = conn.cursor()
            sql = "INSERT INTO Categorias (nome_categoria, descricao_categoria) VALUES (%s, %s)"
            val = (nome_categoria, descricao_categoria)
            cursor.execute(sql, val)
            conn.commit()
            id_nova_categoria = cursor.lastrowid
            return {
                'id_categoria': id_nova_categoria,
                'nome_categoria': nome_categoria,
                'descricao_categoria': descricao_categoria
            }
        except Error as e:

            current_app.logger.error(f"Erro no repositório ao criar categoria '{nome_categoria}': {e}")

            raise e
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    # --- Futuramente, adicionaremos outros métodos aqui ---
    # def buscar_por_id(self, id_categoria):
    #     pass
    #
    # def atualizar(self, id_categoria, nome_categoria, descricao_categoria):
    #     pass
    #
    # def deletar(self, id_categoria):
    #     pass
    # hii