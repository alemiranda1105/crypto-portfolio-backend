from fastapi import FastAPI

from app.server.routes import user, portfolio

app = FastAPI()
app.include_router(user.router)
app.include_router(portfolio.router)


@app.get("/")
async def root():
    return {
        "Welcome": "to portfolio app API"
    }
