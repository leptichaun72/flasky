from flask import Flask, render_template, url_for
from datetime import datetime
 
app = Flask(__name__)
doodaadee = 10002

@app.route('/')
def index():
    print(f'mah date: {doodaadee}')
    return render_template('index.html', foo=doodaadee)
    

app.run ()

