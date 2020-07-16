from flask import render_template, request, redirect, url_for

from app import app, db
from app.models import ToDo


@app.route('/')
def index():
    todo_list = ToDo.query.all()
    return render_template('index.html', todo_list=todo_list)


@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('content')
    if content == '':
        todo_list = ToDo.query.all()
        return render_template('index.html', message='Please enter required '
                                                     'fields', todo_list=todo_list)
    elif len(content) > 255:
        todo_list = ToDo.query.all()
        return render_template('index.html', message='The text is very long.', todo_list=todo_list)
    else:
        todo = ToDo(content=content)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
