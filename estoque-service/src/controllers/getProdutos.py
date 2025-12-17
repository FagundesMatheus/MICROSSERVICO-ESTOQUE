from src.database import get_session
from src.model import Produto


def getProdutos(session):

    return session.query(Produto).all()

