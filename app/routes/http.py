# app/routes/http.py
#Para rodar App python -m uvicorn app.main:app

from fastapi import APIRouter
#from ..manager import ConnectionManager
#from ..database import get_history

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Bem-vindo! Concte-se em /ws/{sala_id}?nickname=SeuNome"}

@router.get("/salas")
async def list_salas():
    return{"message": "Aqui teremos as salas"}


@router.get("/histprico/{sala_id}")
async def history(sala_id: str):
    return {"message": "Aqui teremos o histórico"}