from src.database import get_session
from src.model import Estoque

def removeEstoque(id:int, quantidade:int, session=None):
    if session is None:
        session = get_session()
        return removeEstoque(id, quantidade, session)
    produto = session.query(Estoque).filter_by(id_produto=id).first()
    if produto.quantidade < quantidade:
        raise ValueError(
            f"Estoque insuficiente: disponível {produto.quantidade}, solicitado {quantidade}."
        )
    produto.quantidade -= quantidade
    session.commit()