from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.controllers.user import retrieve_user, sign_up
from app.server.models.response import ResponseModel
from app.server.models.user import UserSchema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/{user_id}")
async def get_user_by_id(user_id):
    users = await retrieve_user(user_id)
    return ResponseModel(users, "User with id {}".format(user_id))


@router.post("/")
async def add_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await sign_up(user)
    return ResponseModel(new_user, "Registro completado")
