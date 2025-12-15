from src.database import get_session
from src.model import Produto


def getProdutos(session=None):
    if session is None:
        session = get_session()
        return getProdutos(session)

    return session.query(Produto).all()

