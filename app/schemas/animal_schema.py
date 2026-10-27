from pydantic import BaseModel, ConfigDict


class AnimalCreate(BaseModel):
    nome: str
    especie: str
    raca: str
    idade: int
    porte: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome": "Rex",
                "especie": "Cachorro",
                "raca": "Caramelo",
                "idade": 3,
                "porte": "Médio"
            }
        }
    )


class AnimalResponse(BaseModel):
    id: int
    nome: str
    especie: str
    raca: str
    idade: int
    porte: str
    status: str = "Disponível"
