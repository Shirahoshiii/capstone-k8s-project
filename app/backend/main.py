from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

DB = "tasks.db"

class Task(BaseModel):
    title: str
    status: str = "pending"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, status TEXT)")
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/tasks")
def get_tasks():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    data = c.fetchall()
    conn.close()
    return data

@app.post("/tasks")
def create_task(task: Task):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (title, status) VALUES (?, ?)", (task.title, task.status))
    conn.commit()
    conn.close()
    return {"msg": "created"}