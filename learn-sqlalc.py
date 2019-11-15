from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)
doodaadee = 10002

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proj.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    print(f'mah date: {doodaadee}')
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', my_tasks=tasks)

if __name__ == "__main__":
    app.run()


