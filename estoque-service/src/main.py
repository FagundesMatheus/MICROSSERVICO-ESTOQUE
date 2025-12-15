
from src.controllers.postProduto import *
from src.controllers.getProdutos import *
from src.controllers.getEstoqueProduto import *


#postProduto("Batata Pringles", "Aquela da boa", 50)
produtos = getProdutos()
for produto in produtos:
    print(produto.nome, produto.id)
p = getEstoqueProduto(15)
print(p.quantidade)