from fastapi import FastAPI
from modules.Cartao.models.cartaoModel import Cartao, DeletarCartao, UpdateCartaoRequest, CartaoPesquisaRequest
from modules.Cartao.controllers.cartaoController import CartaoController

app = FastAPI(title="Api REST Cartao", version="0.0.1" ,
              description="Api para utilização dos cartões de Rapha e Rhai")

@app.get("/v1/cartao",tags=["Cartão"], 
         summary="Visualizar todo uso." )
def visualizar():
    return CartaoController.visualizar_todo_uso()

@app.get("/v1/cartao/pesquisar" , 
         tags=["Cartão"], 
         summary="Pequisar por qualquer parametro enviado no body.")
def visualizar_por_pesquisa(cartao: CartaoPesquisaRequest ):
    return CartaoController.visualizar_por_campos(cartao)
    

@app.post("/v1/cartao/criar",
          tags=["Cartão"], 
          summary="Criar utilização.")
def criar(c: Cartao):
    return CartaoController.criar_utilizacao(c.nome, c.local, c.valor, c.data, c.cartao, c.parcelado)

@app.delete("/v1/cartao/deletar", tags=["Cartão"], 
            summary="Deletar registro feito por ID(s)")
def deletar(cartao: DeletarCartao):
    return CartaoController.deletar_uso(cartao.ids)

@app.put("/v1/cartao/modificar", tags=["Cartão"], 
         summary="Modificar qualquer campo do registro, sendo necessario informar o id")
def modificar(cartaoUpdate: UpdateCartaoRequest):
    return CartaoController.modificar_uso(cartaoUpdate)
    

