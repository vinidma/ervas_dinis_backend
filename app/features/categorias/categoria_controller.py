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

@categoria_bp.route('/', methods=['GET'])
def listar_categorias():
    """
    Endpoint para listar todas as categorias.
    Acessível via GET http://localhost:5000/api/v1/categorias/
    """
    try:
        # 1. Pega o serviço que já foi injetado no contexto 'g'
        categorias_objetos = g.categoria_service.listar_todas_categorias()

        # 2. Transforma a lista de objetos Categoria em uma lista de dicionários
        categorias_dict = [categoria.to_dict() for categoria in categorias_objetos]

        # 3. Retorna a lista em formato JSON
        return jsonify(categorias_dict), 200  # 200 OK

    except Exception as e:
        # Lembre-se de importar o logging no topo do arquivo se quiser usar
        # import logging
        # logging.error(f"Erro ao listar categorias: {e}")
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500

@categoria_bp.route('/<int:id>', methods=['GET'])
def obter_categoria(id: int):
    """
    Endpoint para buscar uma categoria específica por seu ID.
    Acessível via GET http://localhost:5000/api/v1/categorias/<id>
    """
    try:
        # Chama o serviço para buscar a categoria. O ID vem da URL.
        categoria_encontrada = g.categoria_service.obter_categoria_por_id(id)

        return jsonify(categoria_encontrada.to_dict()), 200  # 200 OK

    except ValueError as e:
        # Se o serviço levantou ValueError (porque não encontrou),
        # nós retornamos um erro 404 Not Found.
        return jsonify({'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500

@categoria_bp.route('/<int:id>', methods=['PUT'])
def atualizar_categoria(id: int):
    """
    Endpoint para atualizar uma categoria existente.
    Acessível via PUT http://localhost:5000/api/v1/categorias/<id>
    """
    dados = request.get_json()
    if not dados:
        return jsonify({'erro': 'Corpo da requisição não pode ser vazio'}), 400

    try:
        # Chama o serviço para realizar a atualização
        categoria_atualizada = g.categoria_service.atualizar_categoria(id, dados)
        return jsonify(categoria_atualizada.to_dict()), 200 # 200 OK

    except ValueError as e:
        # O serviço levanta ValueError tanto para "Não Encontrado" quanto para dados inválidos
        # Um status 404 é para "Não encontrado", 400 para "Requisição ruim"
        if "não encontrada" in str(e):
            return jsonify({'erro': str(e)}), 404
        else:
            return jsonify({'erro': str(e)}), 400
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500

@categoria_bp.route('/<int:id>', methods=['DELETE'])
def deletar_categoria(id: int):
    """
    Endpoint para deletar uma categoria.
    Acessível via DELETE http://localhost:5000/api/v1/categorias/<id>
    """
    try:
        g.categoria_service.deletar_categoria(id)

        # Resposta padrão para um DELETE bem-sucedido.
        # Significa "A operação foi um sucesso e não há conteúdo para retornar".
        return '', 204

    except ValueError as e:
        # Reutilizamos a mesma lógica de erro para "Não Encontrado".
        return jsonify({'erro': str(e)}), 404
    except Exception as e:
        return jsonify({'erro': f'Ocorreu um erro interno: {e}'}), 500