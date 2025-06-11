class Produto:
    def __init__(self, nome: str, preco: float, categoria_id: int, descricao: str = "", estoque: int = 0, id: int = None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.categoria_id = categoria_id

    def to_dict(self):
        """Converte o objeto para um dicionário, útil para o JSON."""
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'estoque': self.estoque,
            'categoria_id': self.categoria_id
        }

    def __repr__(self):
        """Representação 'oficial' do objeto, útil para debug."""
        return f"<Produto(id={self.id}, nome='{self.nome}')>"