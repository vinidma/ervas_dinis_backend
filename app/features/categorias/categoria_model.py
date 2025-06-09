# app/features/categorias/categoria_model.py

class Categoria:
    def __init__(self, nome: str, descricao: str, id: int = None):
        self.id = id
        self.nome = nome
        self.descricao = descricao

    def __repr__(self):
        """Representação 'oficial' do objeto, útil para debug."""
        return f"<Categoria(id={self.id}, nome='{self.nome}')>"

    def to_dict(self):
        """Converte o objeto para um dicionário, útil para o JSON."""
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao
        }