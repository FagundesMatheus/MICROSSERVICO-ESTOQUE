from src.database import get_session
from src.model import Estoque


def getEstoqueProduto(id:int, session=None):
    if session is None:
        session = get_session()
        return getEstoqueProduto(id, session)

    return session.query(Estoque).filter_by(id_produto=id).first()
