
from fastapi import FastAPI
from app.schemas.animal_schema import AnimalCreate, AnimalResponse

app = FastAPI(
    title="API Adoção de Animais",
    version="1.0.0",
    description="API REST para gerenciamento de animais disponíveis para adoção."
)

animais = []
proximo_id = 1


@app.get("/", summary="Início")
def inicio():
    return {"mensagem": "API Adoção de Animais funcionando!"}


@app.post(
    "/animais",
    response_model=AnimalResponse,
    status_code=201,
    summary="Cadastrar Animal"
)
def cadastrar_animal(animal: AnimalCreate):
    global proximo_id

    novo_animal = {
        "id": proximo_id,
        **animal.model_dump()
    }

    animais.append(novo_animal)
    proximo_id += 1

    return novo_animal
