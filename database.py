import sqlite3

DB_NAME = "tasks.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_task(description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, done FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_done(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
