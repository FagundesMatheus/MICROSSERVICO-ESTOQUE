from src.model import Reserva
from src.controllers.getEstoqueProduto import getEstoqueProduto
from src.controllers.removeEstoque import removeEstoque


def postReserva(idproduto:int, idpedido:int, quantidade:int, session):

    produto = getEstoqueProduto(idproduto, session)
    if produto.quantidade < quantidade:
        raise ValueError(
            f"Estoque insuficiente: disponível {produto.quantidade}, solicitado {quantidade}."
        )
    reserva = Reserva(idproduto=idproduto, idpedido=idpedido, quantidade=quantidade)
    session.add(reserva)

    removeEstoque(idproduto, quantidade, session)