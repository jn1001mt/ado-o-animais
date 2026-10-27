from pydantic import BaseModel


class AnimalCreate(BaseModel):
    nome: str
    especie: str
    raca: str
    idade: int
    porte: str


class AnimalResponse(BaseModel):
    id: int
    nome: str
    especie: str
    raca: str
    idade: int
    porte: str
    status: str = "Disponível"