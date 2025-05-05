from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from app.models.task_model import get_all_tasks, add_task, get_task, update_task, delete_task

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/')
def index():
    tasks = get_all_tasks()
    return render_template('index.html', tasks=tasks)

@task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task_view():
    if request.method == 'POST':
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'due_date': request.form['due_date'],
            'status': request.form['status'],
            'remarks': request.form['remarks'],
            'created_on': now,
            'updated_on': now,
            'created_by': 'Admin',
            'updated_by': 'Admin'
        }
        add_task(task_data)
        return redirect(url_for('task_bp.index'))
    return render_template('add_task.html')

@task_bp.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
def update_task_view(task_id):
    if request.method == 'POST':
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'due_date': request.form['due_date'],
            'status': request.form['status'],
            'remarks': request.form['remarks'],
            'updated_on': now,
            'updated_by': 'Admin'
        }
        update_task(task_id, task_data)
        return redirect(url_for('task_bp.index'))
    
    task = get_task(task_id)
    return render_template('update_task.html', task=task)

@task_bp.route('/delete_task/<int:task_id>')
def delete_task_view(task_id):
    delete_task(task_id)
    return redirect(url_for('task_bp.index'))