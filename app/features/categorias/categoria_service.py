from .categoria_model import Categoria
from .categoria_repository import CategoriaRepository

class CategoriaService:
    def __init__(self, categoria_repository: CategoriaRepository):
        """
        Inicializa o serviço com uma instância do repositório.
        """
        self.categoria_repository = categoria_repository

    def criar_nova_categoria(self, nome: str, descricao: str) -> Categoria:
        """
        Contém a lógica de negócio para criar uma nova categoria.
        """
        # REGRA DE NEGÓCIO (Exemplo): Futuramente, poderíamos verificar aqui
        # se já existe uma categoria com este nome antes de tentar criar.
        # if self.categoria_repository.buscar_por_nome(nome):
        #     raise ValueError("Uma categoria com este nome já existe.")

        # Orquestração: Cria a instância do modelo
        nova_categoria = Categoria(nome=nome, descricao=descricao)

        # Chama a camada de dados para persistir o objeto
        categoria_criada = self.categoria_repository.criar(nova_categoria)

        return categoria_criada

    # --- Outros métodos de serviço aqui ---
    # def obter_categoria_por_id(self, id: int):
    #     pass



    def listar_todas(self) -> list['Categoria']:
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

            # Importe a classe Categoria no início do arquivo se ainda não o fez:
            # from .categoria_model import Categoria

            # Transforma cada registro do banco em um objeto Categoria
            categorias = [
                Categoria(id=r['id'], nome=r['nome_categoria'], descricao=r['descricao_categoria'])
                for r in registros_db
            ]

            return categorias

        except Exception as e:
            print(f"Erro no repositório ao listar categorias: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()