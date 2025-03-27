from fastapi.responses import JSONResponse
from fastapi import status

class ResponsesOK:
    @classmethod
    def visualizar_todos(cls, results):
        return JSONResponse(status_code=status.HTTP_200_OK ,
                            content={"Utilizacao": [dict(row) for row in results]})
    
    @classmethod
    def inserir_uso(cls, nome, local):
        return JSONResponse(status_code=status.HTTP_201_CREATED , 
                            content={"code": 201, "message": f"Uso cadastrado para {nome} em {local}"})
    
    @classmethod
    def deletar_uso(cls):
        return JSONResponse(status_code=status.HTTP_200_OK, 
                            content={"code" : 200, "message": "Utizações selecionadas deletadas com sucesso!"})