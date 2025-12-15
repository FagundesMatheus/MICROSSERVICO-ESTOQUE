from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class Produto(Base):
    __tablename__ = 'produto'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(30), unique=True)
    descricao: Mapped[str] = mapped_column(String(50))

class Estoque(Base):
    __tablename__ = 'estoque'
    id_produto: Mapped[int] = mapped_column(ForeignKey(Produto.id), primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer)

class Reserva(Base):
    __tablename__ = 'reserva'
    id_produto: Mapped[int] = mapped_column(ForeignKey(Produto.id), primary_key=True)
    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantidade: Mapped[int] = mapped_column(Integer)
