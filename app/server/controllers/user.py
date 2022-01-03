from bson import ObjectId

from app.server.database import user_collection, user_helper


async def retrieve_user(user_id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)


async def sign_up(user_data):
    email_exists = await user_collection.find_one({"email": user_data["email"]})
    if email_exists:
        return False
    else:
        user = await user_collection.insert_one(user_data)
        new_user = await user_collection.find_one({"_id": user.inserted_id})
        return user_helper(new_user)


async def login(user_data):
    user = await user_collection.find_one({"email": user_data["email"]})
    if user:
        if user['password'] == user_data["password"]:
            return user_helper(user)
        else:
            return False
    return False
