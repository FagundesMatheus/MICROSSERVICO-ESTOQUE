from typing import Optional
from pydantic import BaseModel, Field


class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=1)
    descricao: Optional[str] = None
    quantidade: int = 0


class ReservaCreate(BaseModel):
    idproduto: int
    idpedido: int
    quantidade: int


class EstoqueChange(BaseModel):
    id: int
    quantidade: int
