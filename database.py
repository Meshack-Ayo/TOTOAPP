import sqlite3



def connect():
    conn = sqlite3.connect("todo.db")
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLER PRIMARY KEY AUTOINCREMENT,
       title TEXT NOT NULL,
       complete INTEGER DEFAULT 0E IF NOT EXISTS tasks (
       id INTEG

    )
    """)   
    conn.commit()
    conn.close()

def add_task(title):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (titile) VALUE(?)", (title))
    conn.commit()
    conn.close()

def get_task():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT *FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def complete_task(task_id):
    comm = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET complete = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELECT BFROM tasks WHERE id =?,"(task_id,))
    conn.commit()
    conn.close()

