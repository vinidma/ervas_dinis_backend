from .produto_model import Produto
from .produto_repository import ProdutoRepository
# Importamos o repositório de categorias para uma validação!
from ..categorias.categoria_repository import CategoriaRepository


class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository, categoria_repository: CategoriaRepository):
        self.produto_repository = produto_repository
        self.categoria_repository = categoria_repository

    def criar_novo_produto(self, dados_produto: dict) -> Produto:
        """
        Contém a lógica de negócio para criar um novo produto.
        """
        # --- REGRA DE NEGÓCIO NOVA ---
        # Antes de criar um produto, vamos validar se a categoria informada existe.
        categoria_id = dados_produto.get('categoria_id')
        categoria = self.categoria_repository.buscar_por_id(categoria_id)
        if not categoria:
            raise ValueError(f"Categoria com ID {categoria_id} não encontrada.")

        # Validação de dados básicos
        nome = dados_produto.get('nome')
        preco = dados_produto.get('preco')
        if not nome or preco is None:
            raise ValueError("Nome e preço são campos obrigatórios.")

        # Cria a instância do modelo
        novo_produto = Produto(
            nome=nome,
            preco=float(preco),
            categoria_id=int(categoria_id),
            descricao=dados_produto.get('descricao', ''),
            estoque=int(dados_produto.get('estoque', 0))
        )

        # Chama a camada de dados para persistir o objeto
        produto_criado = self.produto_repository.criar(novo_produto)
        return produto_criado