##############
# DATABASE
##############
import os
import random
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "proj.db"))

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,\
    render_template,\
    request,\
    redirect,\
    url_for,\
    make_response,\
    send_file,\
    jsonify
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'exampledude'
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

########
# APP
########
@app.route('/')
def index():
    return "You are not logged in <br><a href = '/login'>" + "click here to log in</a>"

@app.route('/login', methods=['POST','GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      print('user type: {}'.format(user)) 
      return render_template('login.html')

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

#########
# OTHER
#########
@app.route('/main')  # a route
def main_page(): # the controller action
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('model.html', my_tasks=tasks)

@app.route('/users/<name>', methods=['POST'])
def create_user(name):
    msg = f'user {name} created'
    return make_response(msg, 205)

@app.route('/users/<name>', methods=['GET'])
def get_user(name):
    msg = f'Hello {name}'
    return make_response(msg, 200)

@app.route('/image')
def get_image():
    filename = 'airplane-sunset.jpg'
    return send_file(filename, mimetype='image/jpg')

movies = {
    1: 'Toy Story',
    2: 'Star Wars',
    3: 'Kung Fu Panda',
    4: 'The Lion King',
    5: 'Ip Man'
}

@app.route('/movies')
def get_movies():
    return movies

# converting tuple to json through jsonify func
@app.route('/movie/random')
def random_movie():
    # returns a tuple e.g. (5, 'Ip Man')
    movie = random.choice(list(movies.items()))
    return jsonify(movie)

@app.route('/stache/<animal>')
def listen_animal(animal):
    sound = f'Hear a {animal} roar!'
    print(type(sound))
    return render_template('roar.html', creature=sound)

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.errorhandler(404)
def cant_find_page(err):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)

