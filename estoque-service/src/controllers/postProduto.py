from src.database import get_session
from src.model import Produto, Estoque


def postProduto(nome:str, descricao:str = None, quantidade:int = 0, session=None):
    if session is None:
        session = get_session()
        return postProduto(nome, descricao, quantidade, session)


    produto = Produto(
        nome=nome,
        descricao=descricao
    )

    session.add(produto)
    session.commit()
    session.refresh(produto)
    estoque = Estoque(
        id_produto=produto.id,
        quantidade=quantidade
    )
    session.add(estoque)
    session.commit()
