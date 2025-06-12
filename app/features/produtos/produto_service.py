import logging
from .produto_model import Produto
from .produto_repository import ProdutoRepository
from ..categorias.categoria_repository import CategoriaRepository


class ProdutoService:
    def __init__(self, produto_repository: ProdutoRepository, categoria_repository: CategoriaRepository):
        self.produto_repository = produto_repository
        self.categoria_repository = categoria_repository

    def criar_novo_produto(self, dados_produto: dict) -> Produto:
        """
        Contém a lógica de negócio para criar um novo produto.
        """
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

    def listar_todos_os_produtos(self) -> list[dict]:
        """
        Busca todos os produtos e os converte para um formato seguro (dicionário).

        Returns:
            list[dict]: Uma lista de dicionários, cada um representando um produto.
        """
        logging.info("Serviço solicitando a listagem de todos os produtos.")

        # Chama o repositório para buscar os objetos Produto
        produtos_orm = self.produto_repository.listar_todos()

        # Converte a lista de objetos para uma lista de dicionários para ser enviada pela API
        produtos_dict = [produto.to_dict() for produto in produtos_orm]

        return produtos_dict

    def buscar_produto_por_id(self, produto_id: int) -> dict | None:
        """
        Busca um produto específico pelo seu ID.

        Args:
            produto_id (int): O ID do produto a ser buscado.

        Returns:
            dict | None: Um dicionário representando o produto se encontrado,
                         caso contrário, None.
        """
        logging.info(f"Serviço buscando produto com ID {produto_id}.")

        # Chama o repositório para buscar o objeto Produto
        produto = self.produto_repository.buscar_por_id(produto_id)

        if produto:
            # Se encontrou, converte para dicionário antes de retornar
            return produto.to_dict()

        # Se não encontrou, retorna None para a camada de controle decidir o que fazer
        return None

    def atualizar_produto(self, produto_id: int, dados_atualizacao: dict) -> dict:
        """
        Valida e atualiza os dados de um produto existente.
        """
        logging.info(f"Serviço iniciando a atualização para o produto ID {produto_id}.")

        # 1. Busca o produto existente no banco de dados.
        produto_existente = self.produto_repository.buscar_por_id(produto_id)
        if not produto_existente:
            raise ValueError(f"Produto com ID {produto_id} não encontrado.")

        # 2. Valida a categoria, se uma nova for fornecida.
        if 'categoria_id' in dados_atualizacao:
            nova_categoria_id = dados_atualizacao['categoria_id']
            categoria = self.categoria_repository.buscar_por_id(nova_categoria_id)
            if not categoria:
                raise ValueError(f"Categoria com ID {nova_categoria_id} não encontrada para atualização.")

        """
        # 3. Atualiza os campos do objeto 'produto_existente' com os novos dados.
        # O método get(campo, valor_padrao) é ótimo aqui. Ele usa o novo valor se existir,
        # ou mantém o valor antigo (valor_padrao) se o campo não foi fornecido.
        """

        produto_existente.nome = dados_atualizacao.get('nome', produto_existente.nome)
        produto_existente.descricao = dados_atualizacao.get('descricao', produto_existente.descricao)
        produto_existente.preco = float(dados_atualizacao.get('preco', produto_existente.preco))
        produto_existente.estoque = int(dados_atualizacao.get('estoque', produto_existente.estoque))
        produto_existente.categoria_id = int(dados_atualizacao.get('categoria_id', produto_existente.categoria_id))

        # 4. Envia o objeto atualizado para o repositório para ser salvo.
        produto_atualizado = self.produto_repository.atualizar(produto_existente)

        return produto_atualizado.to_dict()

    def deletar_produto(self, produto_id: int):
        """
        Deleta um produto pelo seu ID.
        Lança um erro se o produto não for encontrado.
        """
        logging.info(f"Serviço iniciando a exclusão do produto ID {produto_id}.")

        # Chama o repositório para deletar e obtém o número de linhas afetadas
        linhas_afetadas = self.produto_repository.deletar(produto_id)

        # Se nenhuma linha foi afetada, significa que o produto não existia.
        if linhas_afetadas == 0:
            raise ValueError(f"Produto com ID {produto_id} não encontrado ou já deletado.")

        logging.info(f"Produto com ID {produto_id} deletado com sucesso pelo serviço.")
        # Não há necessidade de retornar nada em uma exclusão bem-sucedida.
