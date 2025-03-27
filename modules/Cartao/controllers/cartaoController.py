from modules.Cartao.database.db import DatabaseCartao
from modules.Cartao.models.cartaoModel import UpdateCartaoRequest, CartaoPesquisaRequest
from modules.Cartao.responses.responsesOK import ResponsesOK
from fastapi import HTTPException

class CartaoController:
    @classmethod
    def visualizar_todo_uso(cls):
        results = DatabaseCartao.query("SELECT * FROM Cartao")
        return ResponsesOK.visualizar_todos(results)
    
    @classmethod
    def visualizar_por_campos(cls, pesquisa: CartaoPesquisaRequest):
        query = "SELECT * FROM Cartao WHERE 1=1"
        params = []

        if pesquisa.nome:
            query += " AND LOWER(Nome) = LOWER(?)"
            params.append(pesquisa.nome)

        if pesquisa.valor is not None:
            query += " AND Valor = ?"
            params.append(pesquisa.valor)

        if pesquisa.local:
            query += " AND LOWER(Local) = LOWER(?)"
            params.append(pesquisa.local)

        if pesquisa.data:
            query += " AND Data = ?"
            params.append(pesquisa.data)

        if pesquisa.cartao:
            query += " AND Cartao = ?"
            params.append(pesquisa.cartao)

        if pesquisa.parcelado is not None:
            query += " AND Parcelado = ?"
            params.append(pesquisa.parcelado)

        results = DatabaseCartao.query(query, tuple(params))
        return ResponsesOK.visualizar_todos(results)
    
    @classmethod
    def criar_utilizacao(cls, nome, local, valor, data, cartao, parcelado):
        DatabaseCartao.query("INSERT INTO Cartao (Nome, Local, Valor, Data, Cartao, Parcelado) VALUES (?, ?, ?, ?, ?, ?)", 
                             (nome, local, valor, data, cartao, parcelado))
        return ResponsesOK.inserir_uso(nome, local)
    
    @classmethod
    def deletar_uso(cls, ids):
        # Se `ids` for um único valor, transforma em uma lista
        if isinstance(ids, (int, str)):
            ids = [ids]
        # Garante que a lista não está vazia
        if not ids:
            raise HTTPException(status_code=400, detail="Nenhum ID fornecido para exclusão.")
        # Cria placeholders dinâmicos (?, ?, ?, ...)
        placeholders = ", ".join(["?" for _ in ids])
        # Executa a query corretamente
        DatabaseCartao.query(f"DELETE FROM Cartao WHERE ID IN ({placeholders})", tuple(ids))
        return {"message": "Registros deletados com sucesso!"}
        
    @classmethod
    def modificar_uso(cls, update_data: UpdateCartaoRequest):
    # Acessar os valores diretamente e filtrar os atributos que são None
        fields_to_update = []
        values = []
    # Itera sobre os campos do UpdateCartaoRequest, excluindo o campo 'id'
        for key, value in update_data.__dict__.items():
            if value is not None:  # Apenas adicionar campos não nulos
                fields_to_update.append(f"{key} = ?")
                values.append(value)   
    # Garantir que o ID também será incluído no final da lista de valores para o WHERE
        values.append(update_data.id)
    # Construa dinamicamente a query
        set_clause = ", ".join(fields_to_update)
        query = f"UPDATE Cartao SET {set_clause} WHERE Id = ?"
    # Execute a query
        DatabaseCartao.query(query, tuple(values))

        return {"message": "Registro atualizado com sucesso!"}
        
        
    
        
        
       

        
        

        
           
   

    
   
    
    
    
        
