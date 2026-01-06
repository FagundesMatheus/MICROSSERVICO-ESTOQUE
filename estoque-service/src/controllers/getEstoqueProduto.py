from src.database import get_session
from src.model import Estoque


def getEstoqueProduto(id:int, session):
    estoque = session.query(Estoque).filter_by(id_produto=id).first()
    if estoque:
        return {
            "id_produto": estoque.id_produto,
            "quantidade": estoque.quantidade
        }
    return None
