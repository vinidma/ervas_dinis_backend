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


    def buscar_por_id(self, id_categoria: int) -> Categoria | None:
        """
        Busca uma categoria específica pelo seu ID.
        Retorna um objeto Categoria ou None se não for encontrada.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "SELECT id, nome_categoria, descricao_categoria FROM categorias WHERE id = ?"

            cursor.execute(sql, (id_categoria,))

            # Pega apenas um resultado da consulta
            registro = cursor.fetchone()

            if registro:
                # Se encontrou um registro, cria e retorna o objeto Categoria
                return Categoria(id=registro['id'], nome=registro['nome_categoria'],
                                 descricao=registro['descricao_categoria'])

            # Se não encontrou nada, retorna None
            return None

        except Exception as e:
            logging.error(f"Erro no repositório ao buscar categoria por ID: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()

    def atualizar(self, categoria: Categoria) -> Categoria:
            """
            Atualiza uma categoria existente no banco de dados.
            Retorna a categoria atualizada.
            """
            cursor = None
            try:
                cursor = self.db_connection.cursor()
                sql = """
                    UPDATE categorias 
                    SET nome_categoria = ?, descricao_categoria = ?
                    WHERE id = ?
                """
                val = (categoria.nome, categoria.descricao, categoria.id)

                cursor.execute(sql, val)
                self.db_connection.commit()

                return categoria

            except Exception as e:
                logging.error(f"Erro no repositório ao atualizar categoria: {e}")
                self.db_connection.rollback()
                raise e
            finally:
                if cursor:
                    cursor.close()

    def deletar(self, id_categoria: int) -> int:
        """
        Deleta uma categoria do banco de dados pelo seu ID.
        Retorna o número de linhas afetadas (1 se deletou, 0 se não encontrou).
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "DELETE FROM categorias WHERE id = ?"

            cursor.execute(sql, (id_categoria,))
            self.db_connection.commit()

            # cursor.rowcount nos diz quantas linhas foram afetadas pelo último comando.
            # Será 1 se a categoria foi encontrada e deletada, e 0 caso contrário.
            return cursor.rowcount

        except Exception as e:
            logging.error(f"Erro no repositório ao deletar categoria: {e}")
            self.db_connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()