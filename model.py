import os

project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)
doodaadee = 10002

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proj.db'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Animal(db.Model):
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)


class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)

	def __init__(self, id, data):
		self.id = id
		self.data = data

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# a route
@app.route('/')

# the controller action
def main_page():
    pass # used as a placeholder
    print(f'mah date: {doodaadee}')
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', my_tasks=tasks)

if __name__ == "__main__":
    app.run()


