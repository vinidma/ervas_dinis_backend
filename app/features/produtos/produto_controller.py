# app/features/produtos/produto_controller.py
from flask import Blueprint, request, jsonify, g


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