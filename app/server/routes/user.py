from fastapi import APIRouter

from app.server.controllers.user import retrieve_user
from app.server.models.response import ResponseModel

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/{user_id}")
async def get_user_by_id(user_id):
    users = await retrieve_user(user_id)
    return ResponseModel(users, "User with id {}".format(user_id))
