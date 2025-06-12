import logging
import sqlite3
from .produto_model import Produto


class ProdutoRepository:
    def __init__(self, db_connection: sqlite3.Connection):
        self.db_connection = db_connection

    def criar(self, novo_produto: Produto) -> Produto:
        """
        Cria um novo produto no banco de dados.
        Retorna o produto criado com o ID preenchido.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = """
                INSERT INTO produtos (nome, descricao, preco, estoque, categoria_id)
                VALUES (?, ?, ?, ?, ?)
            """
            val = (novo_produto.nome, novo_produto.descricao, novo_produto.preco, novo_produto.estoque,
                   novo_produto.categoria_id)

            cursor.execute(sql, val)
            self.db_connection.commit()

            novo_produto.id = cursor.lastrowid
            logging.info(f"Produto criado com sucesso: ID {novo_produto.id}")
            return novo_produto

        except Exception as e:
            logging.error(f"Erro no repositório ao criar produto: {e}")
            self.db_connection.rollback()
            raise e
        finally:
            # Garante que o cursor será fechado, não importa o que aconteça
            if cursor:
                cursor.close()

    def listar_todos(self) -> list[Produto]:
        """
        Lista todos os produtos cadastrados no banco de dados.
        Retorna uma lista de objetos Produto.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id, nome, descricao, preco, estoque, categoria_id FROM produtos")
            rows = cursor.fetchall()

            produtos = [
                Produto(id=row[0], nome=row[1], descricao=row[2], preco=row[3], estoque=row[4], categoria_id=row[5]) for
                row in rows]

            logging.info(f"Listagem de todos os produtos retornou {len(produtos)} registros.")
            return produtos

        except Exception as e:
            logging.error(f"Erro no repositório ao listar produtos: {e}")
            raise e
        finally:
            # Garante que o cursor será fechado
            if cursor:
                cursor.close()

    def buscar_por_id(self, produto_id: int) -> Produto | None:
        """
        Busca um produto específico pelo seu ID.
        Retorna um objeto Produto se encontrado, caso contrário, None.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT id, nome, descricao, preco, estoque, categoria_id FROM produtos WHERE id = ?",
                           (produto_id,))
            row = cursor.fetchone()  # Usamos fetchone() pois esperamos apenas um resultado

            if row:
                logging.info(f"Produto com ID {produto_id} encontrado.")
                return Produto(id=row[0], nome=row[1], descricao=row[2], preco=row[3], estoque=row[4],
                               categoria_id=row[5])

            logging.warning(f"Produto com ID {produto_id} não encontrado no repositório.")
            return None

        except Exception as e:
            logging.error(f"Erro no repositório ao buscar produto por ID {produto_id}: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()

    def atualizar(self, produto: Produto) -> Produto:
        """
        Atualiza os dados de um produto no banco de dados.
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = """
                UPDATE produtos
                SET nome = ?, descricao = ?, preco = ?, estoque = ?, categoria_id = ?
                WHERE id = ?
            """
            val = (produto.nome, produto.descricao, produto.preco, produto.estoque, produto.categoria_id, produto.id)

            cursor.execute(sql, val)
            self.db_connection.commit()

            logging.info(f"Produto com ID {produto.id} atualizado com sucesso.")
            return produto

        except Exception as e:
            logging.error(f"Erro no repositório ao atualizar produto com ID {produto.id}: {e}")
            self.db_connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()

    def deletar(self, produto_id: int) -> int:
        """
        Deleta um produto do banco de dados pelo seu ID.
        Retorna o número de linhas afetadas (1 se sucesso, 0 se não encontrado).
        """
        cursor = None
        try:
            cursor = self.db_connection.cursor()
            sql = "DELETE FROM produtos WHERE id = ?"
            cursor.execute(sql, (produto_id,))
            self.db_connection.commit()

            # cursor.rowcount nos diz quantas linhas foram afetadas pela operação
            num_linhas_afetadas = cursor.rowcount
            logging.info(f"{num_linhas_afetadas} linha(s) deletada(s) para o produto ID {produto_id}.")
            return num_linhas_afetadas

        except Exception as e:
            logging.error(f"Erro no repositório ao deletar produto com ID {produto_id}: {e}")
            self.db_connection.rollback()
            raise e
        finally:
            if cursor:
                cursor.close()