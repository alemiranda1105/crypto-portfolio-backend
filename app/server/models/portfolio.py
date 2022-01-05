from typing import Optional, List

from pydantic import BaseModel, Field

from app.server.models.coin import CoinSchema


class PortfolioSchema(BaseModel):
    class Coin(BaseModel):
        qty: float = Field(...)
        symbol: str = Field(...)
        name: str = Field(...)

    user_id: str = Field(...)
    coins: List[Coin] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "1",
                "coins": [
                    {
                        "name": "Bitcoin",
                        "symbol": "BTC",
                        "qty": 0.36
                    },
                    {
                        "name": "Solana",
                        "symbol": "SOL",
                        "qty": 1.74
                    }
                ]
            }
        }


class UpdatePortfolioModel(BaseModel):
    user_id: Optional[str]
    coins: Optional[List[CoinSchema]]

    class Config:
        schema_extra = {
            "example": {
                "user_id": "1",
                "coins": [
                    {
                        "name": "Bitcoin",
                        "symbol": "BTC",
                        "qty": 0.36
                    },
                    {
                        "name": "Solana",
                        "symbol": "SOL",
                        "qty": 1.74
                    }
                ]
            }
        }
