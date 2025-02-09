from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import hash_password, verify_password, create_access_token, verify_token
from database import get_db, engine
from models import User, Base
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskBoard API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_mail = db.query(User).filter(User.email == user.email).first()
    if existing_mail:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@app.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/")
def get_users(payload: dict = Depends(verify_token), db: Session = Depends(get_db)):
    print(payload)
    users = db.query(User).all()
    return users
