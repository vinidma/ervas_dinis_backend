# app/features/produtos/produto_controller.py
from flask import Blueprint, request, jsonify, g
import logging

produto_bp = Blueprint('produtos', __name__, url_prefix='/api/v1/produtos')

@produto_bp.route('/', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Corpo da requisição não pode ser vazio'}), 400

    try:
        # O serviço é pego do contexto 'g', como fizemos para categorias
        novo_produto = g.produto_service.criar_novo_produto(dados)
        return jsonify(novo_produto.to_dict()), 201

    except ValueError as e:
        # Captura erros de validação, como categoria não encontrada ou campos faltando
        return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500


# --- ENDPOINT PARA LISTAR TODOS OS PRODUTOS ---
@produto_bp.route('/', methods=['GET'])
def listar_produtos():
    """
    Endpoint para listar todos os produtos cadastrados.
    """
    logging.info("Requisição recebida para listar todos os produtos.")
    try:
        # Usando o mesmo padrão para acessar o serviço
        lista_de_produtos = g.produto_service.listar_todos_os_produtos()
        return jsonify(lista_de_produtos), 200 # 200 OK

    except Exception as e:
        # Em caso de um erro inesperado no serviço ou repositório
        logging.error(f"Erro inesperado no servidor ao listar produtos: {e}")
        return jsonify({'erro': 'Ocorreu um erro inesperado no servidor.'}), 500


@produto_bp.route('/<int:produto_id>', methods=['GET'])
def buscar_produto(produto_id: int):
    """
    Endpoint para buscar um produto específico pelo seu ID.
    O ID é passado como parte da URL.
    """
    logging.info(f"Requisição recebida para buscar produto com ID {produto_id}.")
    try:
        # Chama o serviço para buscar o produto
        produto = g.produto_service.buscar_produto_por_id(produto_id)

        if produto:
            # Se o serviço retornou um produto, envia como resposta
            return jsonify(produto), 200  # 200 OK
        else:
            # Se o serviço retornou None, significa que não foi encontrado
            return jsonify({'erro': f'Produto com ID {produto_id} não encontrado.'}), 404  # 404 Not Found

    except Exception as e:
        logging.error(f"Erro inesperado no servidor ao buscar produto por ID {produto_id}: {e}")
        return jsonify({'erro': 'Ocorreu um erro inesperado no servidor.'}), 500


@produto_bp.route('/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id: int):
    """
    Endpoint para atualizar um produto existente.
    """
    dados_recebidos = request.get_json()
    if not dados_recebidos:
        return jsonify({'erro': 'Corpo da requisição não pode ser vazio'}), 400

    logging.info(f"Requisição recebida para atualizar o produto ID {produto_id} com os dados: {dados_recebidos}")
    try:
        # O serviço já lida com a lógica de buscar e validar
        produto_atualizado = g.produto_service.atualizar_produto(produto_id, dados_recebidos)
        return jsonify(produto_atualizado), 200  # 200 OK

    except ValueError as e:
        # Erros de validação (ex: produto não encontrado, categoria inválida)
        # O serviço lança ValueError, que aqui se traduz em um erro 404 ou 400.
        # Para o cliente, um 'não encontrado' é mais específico.
        if "não encontrado" in str(e):
            return jsonify({'erro': str(e)}), 404  # 404 Not Found
        else:
            return jsonify({'erro': str(e)}), 400  # 400 Bad Request

    except Exception as e:
        logging.error(f"Erro inesperado no servidor ao atualizar produto ID {produto_id}: {e}")
        return jsonify({'erro': 'Ocorreu um erro inesperado no servidor.'}), 500

@produto_bp.route('/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id: int):
    """
    Endpoint para deletar um produto existente.
    """
    logging.info(f"Requisição recebida para deletar o produto ID {produto_id}.")
    try:
        # O serviço lida com a lógica de deletar e de verificar se existia.
        g.produto_service.deletar_produto(produto_id)
        # Para DELETE, um sucesso é geralmente um '204 No Content' com corpo vazio.
        return '', 204

    except ValueError as e:
        # O serviço lança ValueError se o produto não for encontrado.
        return jsonify({'erro': str(e)}), 404 # 404 Not Found

    except Exception as e:
        logging.error(f"Erro inesperado no servidor ao deletar produto ID {produto_id}: {e}")
        return jsonify({'erro': 'Ocorreu um erro inesperado no servidor.'}), 500
