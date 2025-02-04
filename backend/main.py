from fastapi import FastAPI
import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskBoard API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}
