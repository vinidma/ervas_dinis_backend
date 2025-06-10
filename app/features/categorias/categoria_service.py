# app/features/categorias/categoria_service.py

from .categoria_model import Categoria
from .categoria_repository import CategoriaRepository

class CategoriaService:

    def __init__(self, categoria_repository: CategoriaRepository):
        """
        Inicializa o serviço com uma instância do repositório.
        """
        self.categoria_repository = categoria_repository

    # ADICIONE INDENTAÇÃO EM TODOS OS MÉTODOS ABAIXO
    def criar_nova_categoria(self, nome: str, descricao: str) -> Categoria:
        """
        Contém a lógica de negócio para criar uma nova categoria.
        """
        # Orquestração: Cria a instância do modelo
        nova_categoria = Categoria(nome=nome, descricao=descricao)

        # Chama a camada de dados para persistir o objeto
        categoria_criada = self.categoria_repository.criar(nova_categoria)

        return categoria_criada

    def listar_todas_categorias(self) -> list['Categoria']:
        """
        Regras de negócio para listar todas as categorias.
        Neste caso simples, apenas repassa a chamada para o repositório.
        """
        return self.categoria_repository.listar_todas()

    def obter_categoria_por_id(self, id_categoria: int) -> Categoria:
        """
        Busca uma categoria pelo ID.
        Levanta um erro se a categoria não for encontrada.
        """
        categoria = self.categoria_repository.buscar_por_id(id_categoria)

        if categoria is None:
            raise ValueError("Categoria não encontrada")

        return categoria

    def atualizar_categoria(self, id_categoria: int, novos_dados: dict) -> Categoria:
        """
        Regras de negócio para atualizar uma categoria.
        """
        categoria_existente = self.obter_categoria_por_id(id_categoria)

        novo_nome = novos_dados.get('nome')
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome não pode ser vazio.")

        categoria_existente.nome = novo_nome
        categoria_existente.descricao = novos_dados.get('descricao', categoria_existente.descricao)

        categoria_atualizada = self.categoria_repository.atualizar(categoria_existente)

        return categoria_atualizada

    def deletar_categoria(self, id_categoria: int):
        """
        Regras de negócio para deletar uma categoria.
        """
        linhas_afetadas = self.categoria_repository.deletar(id_categoria)

        if linhas_afetadas == 0:
            raise ValueError("Categoria não encontrada")