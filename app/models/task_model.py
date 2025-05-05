from app.db import get_db_connection
from datetime import datetime

def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks ORDER BY id DESC')
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def get_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    cursor.close()
    conn.close()
    return task

def add_task(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, status, remarks, created_on, updated_on, created_by, updated_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        data['title'], data['description'], data['due_date'],
        data['status'], data['remarks'], data['created_on'],
        data['updated_on'], data['created_by'], data['updated_by']
    ))
    conn.commit()
    cursor.close()
    conn.close()

def update_task(task_id, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks 
        SET title=%s, description=%s, due_date=%s, status=%s, remarks=%s, updated_on=%s, updated_by=%s
        WHERE id=%s
    ''', (
        data['title'], data['description'], data['due_date'],
        data['status'], data['remarks'], data['updated_on'],
        data['updated_by'], task_id
    ))
    conn.commit()
    cursor.close()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    cursor.close()
    conn.close()