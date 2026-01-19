from typing import Generator

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from src.controllers.getReserva import getReservasPedido, getReservaPedidoProduto
from src.controllers.getProdutos import getProdutos
from src.controllers.getEstoqueProduto import getEstoqueProduto
from src.controllers.postProduto import postProduto
from src.controllers.postReserva import postReserva
from src.controllers.addEstoque import addEstoque
from src.controllers.removeEstoque import removeEstoque
from src.controllers.deleteReserva import deleteReservaPedidoProduto
from src.schemas import ProdutoCreate, ReservaCreate, EstoqueChange
from src.database import get_session
from src.controllers.deleteProduto import deleteProduto


def get_db() -> Generator:
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


app = FastAPI(title="estoque-service", version="0.1.0")


@app.exception_handler(ValueError)
def value_error_handler(request, exc: ValueError):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(exc)})


@app.exception_handler(SQLAlchemyError)
def sqlalchemy_error_handler(request, exc: SQLAlchemyError):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "database_error"})


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/produtos")
def listar_produtos(db=Depends(get_db)):
    return getProdutos(db)


@app.get("/estoque/{id}")
def listar_estoque_produto(id: int, db=Depends(get_db)):
    data = getEstoqueProduto(id, db)
    if data is None:
        raise HTTPException(status_code=404, detail="not_found")
    return data


@app.get("/reserva/{id_pedido}")
def listar_reservas_pedido(id_pedido: int, db=Depends(get_db)):
    return getReservasPedido(id_pedido, db)


@app.get("/reserva/{id_pedido}/{id_produto}")
def listar_reserva_pedido_produto(id_pedido: int, id_produto: int, db=Depends(get_db)):
    data = getReservaPedidoProduto(id_pedido, id_produto, db)
    if data is None:
        raise HTTPException(status_code=404, detail="not_found")
    return data


@app.post("/produto", status_code=status.HTTP_201_CREATED)
def criar_produto(payload: ProdutoCreate, db=Depends(get_db)):
    postProduto(db, payload.nome, payload.descricao, payload.quantidade)
    return {"message": "produto_criado"}


@app.post("/reserva", status_code=status.HTTP_201_CREATED)
def criar_reserva(payload: ReservaCreate, db=Depends(get_db)):
    postReserva(payload.idproduto, payload.idpedido, payload.quantidade, db)
    return {"message": "reserva_criada"}


@app.post("/estoque/adicionar")
def adicionar_estoque(payload: EstoqueChange, db=Depends(get_db)):
    addEstoque(payload.id, payload.quantidade, db)
    return {"message": "estoque_atualizado"}


@app.post("/estoque/remover")
def remover_estoque(payload: EstoqueChange, db=Depends(get_db)):
    removeEstoque(payload.id, payload.quantidade, db)
    return {"message": "estoque_atualizado"}


@app.delete("/reserva/{id_pedido}/{id_produto}")
def deletar_reserva(id_pedido: int, id_produto: int, db=Depends(get_db)):
    deleteReservaPedidoProduto(id_pedido, id_produto, db)
    return {"message": "reserva_deletada"}

@app.delete("/produto/{id_produto}")
def deletar_produto(id_produto: int, db=Depends(get_db)):
    deleteProduto(id_produto, db)
    return {"message": "produto_deletado"}

