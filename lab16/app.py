from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

#--------------
#database config
#--------------

DB_PATH = 'todo_db.db'

def get_db():
    """Get database connection"""
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """Initialize database with sample tasks"""
    if not os.path.exists(DB_PATH):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            )
        ''')
        # Add sample tasks
        cursor.execute("INSERT INTO tasks (task) VALUES ('clean the house')")
        cursor.execute("INSERT INTO tasks (task) VALUES ('complete lab task')")
        db.commit()
        cursor.close()
        db.close()

# Initialize database on startup
init_db()

#----------------
# Home route
#----------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    try:
        database = get_db()
        cursor = database.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        database.close()
        return jsonify([dict(task) for task in tasks])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#----------------
# add new task
#----------------
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')

    if task:
        try:
            database = get_db()
            cursor = database.cursor()
            cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            database.commit()
            cursor.close()
            database.close()
            return jsonify({'status': 'success'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    else:
        return jsonify({'status': 'error'})

# delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    task_id = data.get('id')

    database = get_db()
    cursor = database.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    database.commit()
    cursor.close()
    database.close()
    return jsonify({'status': 'deleted'})
    


#----------------
#run app
#----------------
if __name__ == '__main__':
    app.run(debug=True)