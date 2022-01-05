from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from app.server.auth.auth_bearer import JWTBearer
from app.server.controllers.portfolio import get_user_portfolio, add_portfolio, update_portfolio, remove_portfolio
from app.server.models.portfolio import PortfolioSchema, UpdatePortfolioModel
from app.server.models.response import ResponseModel, ErrorResponseModel

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolios"],
    dependencies=[Depends(JWTBearer())]
)


@router.get("/{user_id}")
async def user_portfolio(user_id):
    portfolio = await get_user_portfolio(user_id)
    return ResponseModel(portfolio, "Porfolio from {}".format(user_id))


@router.post("/")
async def create_portfolio(data: PortfolioSchema = Body(...)):
    data = jsonable_encoder(data)
    new_portfolio = await add_portfolio(data)
    return ResponseModel(new_portfolio, "Portfolio added")


@router.patch("/{port_id}")
async def update(port_id: str, data: UpdatePortfolioModel = Body(...)):
    req = {key: value for key, value in data.dict().items() if value is not None}
    updated = await update_portfolio(port_id, req)
    if not updated:
        return ErrorResponseModel("Error updating your portfolio", 400, "Something went wrong")
    else:
        return ResponseModel(updated)


@router.delete("/{port_id}")
async def remove(port_id: str):
    removed = await remove_portfolio(port_id)
    if removed:
        return ResponseModel({"removed": True}, "Portfolio removed")
    else:
        return ErrorResponseModel("Error updating your portfolio", 400, "Something went wrong")
