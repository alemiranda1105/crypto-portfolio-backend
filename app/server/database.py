import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017/crypto"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.crypto

user_collection = db.get_collection("users")
portfolio_collection = db.get_collection("portfolios")


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": str(user["email"])
    }


def portfolio_helper(portfolio) -> dict:
    return {
        "id": str(portfolio["_id"]),
        "user_id": str(portfolio["user_id"]),
        "coins": portfolio["coins"]
    }
