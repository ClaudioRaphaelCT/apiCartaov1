from pydantic import BaseModel, Field
from typing import List, Optional

class Cartao(BaseModel):
    nome: str
    local: str
    valor: float
    data: str
    cartao: str
    parcelado: int = Field(..., ge=0, le=1)  # ✅ Restringe para 0 ou 1 (0 = False, 1 = True)

class CartaoPesquisaRequest(BaseModel):
    nome: Optional[str] = None
    local: Optional[str] = None
    valor: Optional[float] = None
    data: Optional[str] = None
    cartao: Optional[str] = None
    parcelado: Optional[int] = None

class DeletarCartao(BaseModel):
    ids: List[int]

class UpdateCartaoRequest(BaseModel):
    id: int 
    nome: Optional[str] = None  
    local: Optional[str] = None 
    valor: Optional[float] = None  
    data: Optional[str] = None  
    cartao: Optional[str] = None 
    parcelado: Optional[int] = Field(None, ge=0, le=1)  


    