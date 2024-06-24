from typing import List

from sqlalchemy import select

import main_config
import os

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from database import User
from database import SessionLocal
from telegram_api_connector.tg_api_manager import TelegramApiManager
from user_model import UserConfig

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user(api_id: str, db: Session = Depends(get_db)) -> User:
    user = db.query(User).filter(User.api_id == api_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_telegram_manager(user: UserConfig = Depends(get_user)) -> TelegramApiManager:
    manager = TelegramApiManager(user)
    await manager.connect()
    return manager


@app.get("/users/", response_model=List[UserConfig])
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/create_user/")
def create_user(user_data: UserConfig, db: Session = Depends(get_db)):
    db_user = db.execute(select(User).filter_by(phone=user_data.phone)).scalar()
    if db_user:
        raise HTTPException(status_code=400, detail="Phone already registered")
    new_user = User(api_id=user_data.api_id, api_hash=user_data.api_hash, phone=user_data.phone)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_data": user_data.dict()}


@app.post("/update_secret_key/")
def update_secret_key(api_id: str, secret_key: str, db: Session = Depends(get_db)):
    db_user = db.execute(select(User).filter_by(api_id=api_id)).scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.secret_key = secret_key
    db.commit()
    db.refresh(db_user)
    return {"message": "Secret key updated successfully", "user_data": {
        "api_id": db_user.api_id,
        "phone": db_user.phone,
        "secret_key": db_user.secret_key
    }}


@app.post("/start_auth/")
async def start_auth(manager: TelegramApiManager = Depends(get_telegram_manager)):
    await manager.authorize()
    return {"message": "Authorization started, please check your phone for the verification code"}


@app.post("/complete_auth/")
async def complete_auth(code: str, manager: TelegramApiManager = Depends(get_telegram_manager)):
    await manager.authorize(code)
    return {"message": "Authorization completed successfully"}


@app.post("/change_avatar/")
async def change_avatar(manager: TelegramApiManager = Depends(get_telegram_manager)):
    await manager.change_avatar()
    return {"message": "Avatar changed successfully"}


@app.on_event("startup")
async def startup_event():
    for directory in main_config.CORE_DIRS:
        if not os.path.exists(directory):
            os.makedirs(directory)
