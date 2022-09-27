from pydantic import BaseModel

class ContasModels(BaseModel):
    id: int
    nome: str
    email: str