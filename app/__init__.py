from flask import Flask, g
from app.db import database

# Importe os novos repositórios e serviços
from app.features.categorias.categoria_repository import CategoriaRepository
from app.features.categorias.categoria_service import CategoriaService
from app.features.produtos.produto_repository import ProdutoRepository
from app.features.produtos.produto_service import ProdutoService


def create_app():
    app = Flask(__name__)

    # ... (código do logger que já existe) ...

    app.teardown_appcontext(database.close_db)

    @app.before_request
    def inject_dependencies():
        conn = database.get_db()

        # Injetando o serviço de categorias (como antes)
        categoria_repo = CategoriaRepository(db_connection=conn)
        g.categoria_service = CategoriaService(categoria_repository=categoria_repo)

        # --- NOVO: Injetando o serviço de produtos ---
        produto_repo = ProdutoRepository(db_connection=conn)
        # Note que passamos os dois repositórios que o ProdutoService precisa
        g.produto_service = ProdutoService(produto_repository=produto_repo, categoria_repository=categoria_repo)

    # Registra o blueprint de categorias (como antes)
    from app.features.categorias.categoria_controller import categoria_bp
    app.register_blueprint(categoria_bp)

    # --- NOVO: Registra o blueprint de produtos ---
    from app.features.produtos.produto_controller import produto_bp
    app.register_blueprint(produto_bp)

    with app.app_context():
        database.init_db()

    # ... (log de inicialização que já existe) ...
    return app