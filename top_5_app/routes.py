  
# Import the app variable from the init
from top_5_app import app

# Import specific packages from flask
from flask import render_template

# Default Home Route
@app.route('/')
def home():
    name = "Top Five Directors"
    return render_template('home.html', name=name)

@app.route('/dir')
def direct():
    director_dict = {1:'Hayo Miyazaki', 2: 'Christopher Nolan', 3: 'Quentin Tarantino', 4: 'Steve McQueen', 5: 'Melina Matsoukas' }
    return render_template('dir.html', director_dict=director_dict)