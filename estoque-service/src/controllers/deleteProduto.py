from src.model import Produto, Estoque


def deleteProduto(idProduto: int, session):
    produto = session.query(Produto).filter_by(id=idProduto).first()
    if not produto:
        return None

    # remover registro de estoque que referencia o produto (evita FK violation)
    estoque = session.query(Estoque).filter_by(id_produto=idProduto).first()
    if estoque:
        session.delete(estoque)

    session.delete(produto)
    return True