from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    # Creates access to database
    connection = sqlite3.connect("to_do_list.db")

    # Enables ability for SQL queries
    db = connection.cursor()

    all_tasks = db.execute("SELECT id, task FROM to_do_list")

    # List of tuples (each tuple contains id and task)
    all_tasks = all_tasks.fetchall()

    return render_template("index.html", all_tasks=all_tasks)


@app.route('/add_task', methods=["GET", "POST"])
def add_task():
    connection = sqlite3.connect("to_do_list.db")
    db = connection.cursor()

    if request.method == "POST":

        task = request.form.get("task")

        # Adds task to database
        db.execute("INSERT INTO to_do_list (task) VALUES (?)", (task,))
        connection.commit()

        return redirect('/')


@app.route('/delete_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    connection = sqlite3.connect("to_do_list.db")
    db = connection.cursor()

    # Remove task from database
    db.execute("DELETE FROM to_do_list WHERE id=?", (task_id,))
    connection.commit()


if __name__ == '__main__':
    app.run()