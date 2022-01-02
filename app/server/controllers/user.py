from bson import ObjectId

from app.server.database import user_collection, user_helper


async def retrieve_user(user_id: str) -> dict:
    print(ObjectId(user_id))

    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    print(user)
    if user:
        return user_helper(user)
