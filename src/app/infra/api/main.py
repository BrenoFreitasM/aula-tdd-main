from fastapi import FastAPI
from infra.api.routers import user_routers


app = FastAPI()

app.include_router(user_routers.router)