from src.database import get_session
from src.model import Reserva
from getEstoqueProduto import getEstoqueProduto
from removeEstoque import removeEstoque


def postReserva(idproduto:int, idpedido:int, quantidade:int, session=None):
    if session is None:
        session = get_session()
        return postReserva(idproduto, idpedido, quantidade, session)

    produto = getEstoqueProduto(idproduto, session)
    if produto.quantidade < quantidade:
        raise ValueError(
            f"Estoque insuficiente: disponível {produto.quantidade}, solicitado {quantidade}."
        )
    reserva = Reserva(idproduto=idproduto, idpedido=idpedido, quantidade=quantidade)
    session.add(reserva)

    removeEstoque(idproduto, quantidade, session)
    session.commit()
