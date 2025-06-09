from flask import Flask, g
from .db import database
from .features.categorias.categoria_repository import CategoriaRepository
from .features.categorias.categoria_service import CategoriaService


def create_app():
    app = Flask(__name__)

    # Garante que a função de fechar o banco seja chamada ao final de cada requisição.
    app.teardown_appcontext(database.close_db)

    # Este hook será executado ANTES de cada requisição.
    @app.before_request
    def inject_dependencies():
        """
        Injeta dependências no contexto 'g' da requisição.
        Isso torna o service e o repository disponíveis para os controllers.
        """
        # A função get_db agora gerencia a conexão para nós.
        conn = database.get_db()

        # Criamos as instâncias uma vez por requisição.
        categoria_repo = CategoriaRepository(db_connection=conn)
        g.categoria_service = CategoriaService(categoria_repository=categoria_repo)

    # Registra o blueprint do controller
    from .features.categorias.categoria_controller import categoria_bp
    app.register_blueprint(categoria_bp)

    # Inicializa o banco de dados (só precisa rodar uma vez ao iniciar)
    with app.app_context():
        database.init_db()

    return app