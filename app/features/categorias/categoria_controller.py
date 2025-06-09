from flask import Blueprint, request, jsonify, g  # Importamos o 'g'


categoria_bp = Blueprint('categorias', __name__, url_prefix='/api/v1/categorias')


@categoria_bp.route('/', methods=['POST'])
def criar_categoria():
    dados = request.get_json()

    if not dados or 'nome' not in dados:
        return jsonify({'erro': 'O campo "nome" é obrigatório'}), 400

    nome = dados.get('nome')
    descricao = dados.get('descricao', '')

    try:
        # Apenas pegamos o serviço que já foi criado para nós e o usamos.
        # Não há mais conn.get, new Repository(), new Service(), conn.close()...
        nova_categoria = g.categoria_service.criar_nova_categoria(nome, descricao)

        return jsonify(nova_categoria.to_dict()), 201

    except ValueError as e:
        return jsonify({'erro': str(e)}), 409
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500