import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017/crypto"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

db = client.crypto

user_collection = db.get_collection("users")


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": str(user["email"])
    }
