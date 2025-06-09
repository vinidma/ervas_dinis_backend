import logging
from .categoria_model import Categoria


class CategoriaRepository:
    def __init__(self, db_connection):
        """
        O repositório recebe a conexão com o banco de dados.
        Ele não a cria, o que o torna mais testável e desacoplado.
        """
        self.db_connection = db_connection

    def criar(self, nova_categoria: Categoria) -> Categoria:
        """
        Cria uma nova categoria no banco de dados.
        Retorna a categoria criada com o ID preenchido.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()

            # ATENÇÃO: Corrigimos o nome das colunas para corresponder ao que criamos no init_db()
            sql = "INSERT INTO categorias (nome_categoria, descricao_categoria) VALUES (?, ?)"

            # Para SQLite, o placeholder é '?' em vez de '%s'
            val = (nova_categoria.nome, nova_categoria.descricao)

            cursor.execute(sql, val)
            self.db_connection.commit()

            id_gerado = cursor.lastrowid
            nova_categoria.id = id_gerado

            logging.info(f"Categoria criada com sucesso: ID {id_gerado}")
            return nova_categoria

        except Exception as e:
            logging.error(f"Erro no repositório ao criar categoria: {e}")
            if self.db_connection:
                self.db_connection.rollback()
            raise e

        finally:
            if cursor:
                cursor.close()

    def listar_todas(self) -> list[Categoria]:
            """
            Busca e retorna todas as categorias do banco de dados.
            Retorna uma lista de objetos Categoria.
            """
            cursor = None
            try:
                cursor = self.db_connection.cursor()

                sql = "SELECT id, nome_categoria, descricao_categoria FROM categorias"
                cursor.execute(sql)

                # Pega todos os resultados da consulta
                registros_db = cursor.fetchall()

                # Transforma cada registro do banco em um objeto Categoria
                categorias = [
                    Categoria(id=r['id'], nome=r['nome_categoria'], descricao=r['descricao_categoria'])
                    for r in registros_db
                ]

                return categorias

            except Exception as e:
                logging.error(f"Erro no repositório ao listar categorias: {e}")
                raise e
            finally:
                if cursor:
                    cursor.close()