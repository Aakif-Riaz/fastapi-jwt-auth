from fastapi import FastAPI
from database import Base, engine

from auth.routes import router as auth_router
from routers.users import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="JWT User Authentication")

app.include_router(auth_router)
app.include_router(user_router)
from dotenv import load_dotenv