import sqlite3

DB_NAME = "tasks.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

# cria a tabela
def create_tables():
    conn = connect_db() # conecta ao banco
    cursor = conn.cursor() # cria um cursor que executa comandos SQL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit() # salva as mudanças no banco
    conn.close() # fecha a conexão com o banco


# add nova tarefa
def add_task(description):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
    conn.commit()
    conn.close()


# listar tarefas
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, description, done FROM tasks")
    tasks = cursor.fetchall() # busca todos os resultados da consulta SQL e retorna em forma de lista de tuplas 
    conn.close()
    return tasks


# marcar tarefa como concluída
def mark_done(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    

def delete_task(task_id):
    conn =  connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()