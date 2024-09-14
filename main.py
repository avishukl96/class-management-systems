# main.py
from fastapi import FastAPI
from app.config.db import engine
from app.models import user, classes, subject, user_role

app = FastAPI()

# Initialize the database tables
def init_db():
    user.Base.metadata.create_all(bind=engine)
    classes.Base.metadata.create_all(bind=engine)
    subject.Base.metadata.create_all(bind=engine)
    user_role.Base.metadata.create_all(bind=engine)

init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Class Management System"}
