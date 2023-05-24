from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db import Base, engine, get_db
from models import Banner
from routers import *


app = FastAPI(title='Anticafe')

Base.metadata.create_all(engine)

app.mount('/uploads', StaticFiles(directory='uploads'), name='uploads')

app.include_router(banner_router)
app.include_router(qa_router)
