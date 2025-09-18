# app/routes/http.py
#Para rodar App python -m uvicorn app.main:app

from fastapi import APIRouter
from ..manager import ConnectionManager
from ..database import salvar_mensagem
router = APIRouter()
manager = ConnectionManager()

@router.get("/")
async def root():
    return {"message": "Bem-vindo! Concte-se em /ws/{sala_id}?nickname=SeuNome"}

@router.get("/salas")
async def list_salas():
    return{sala_id: list(nicks.values()) for sala_id, nicks in manager.salas.items()}


@router.get("/histprico/{sala_id}")
async def history(sala_id: str):
    return {"message": "Aqui teremos o histórico"}


@router.get("/teste")
async def teste():
    salvar_mensagem(1, "Lary", "hello")
    return{"message": "Aqui teremos as salas"}