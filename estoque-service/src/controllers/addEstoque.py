from src.database import get_session
from src.model import Estoque


def addEstoque(id:int, quantidade:int, session):

    produto = session.query(Estoque).filter_by(id_produto=id).first()
    produto.quantidade += quantidade



