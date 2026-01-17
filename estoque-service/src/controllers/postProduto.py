from src.model import Produto, Estoque


def postProduto(session, nome:str, descricao:str = None,  quantidade:int = 0):

    produto = Produto(
        nome=nome,
        descricao=descricao
    )

    session.add(produto)
    session.flush()
    estoque = Estoque(
        id_produto=produto.id,
        quantidade=quantidade
    )
    session.add(estoque)
