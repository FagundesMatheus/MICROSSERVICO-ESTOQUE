from src.model import Produto


def getProdutos(session):
    produtos = session.query(Produto).all()
    return [
        {
            "id": p.id,
            "nome": p.nome,
            "descricao": p.descricao
        }
        for p in produtos
    ]

