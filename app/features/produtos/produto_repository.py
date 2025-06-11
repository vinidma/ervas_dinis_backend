import logging
from .produto_model import Produto


class ProdutoRepository:
    def __init__(self, db_connection):
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
            if cursor:
                cursor.close()