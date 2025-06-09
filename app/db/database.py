import sqlite3
from flask import g # Importamos o 'g'

DATABASE_FILE = "ervasdinis.db"

def get_db():
    """
    Cria uma conexão com o banco de dados se não houver uma no contexto atual.
    Reutiliza a conexão existente se já houver.
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_FILE)
        db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    """Fecha a conexão com o banco de dados se ela existir."""
    db = g.pop('_database', None)
    if db is not None:
        db.close()

def init_db():
    """Inicializa o banco de dados e cria as tabelas."""
    # Usamos with para garantir que a conexão seja fechada mesmo se houver erro
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_categoria TEXT NOT NULL UNIQUE,
            descricao_categoria TEXT
        );
        """)
        conn.commit()
    print("Banco de dados inicializado.")