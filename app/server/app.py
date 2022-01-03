from fastapi import FastAPI

from app.server.routes import user

app = FastAPI()
app.include_router(user.router)

@app.get("/")
async def root():
    return {
        "Welcome": "to portfolio app API"
    }
