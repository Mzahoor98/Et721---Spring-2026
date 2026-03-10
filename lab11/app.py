"""
Muhammad Zahoor
lab 11, introduction to Flask
March 10, 2026
"""
from flask import Flask, render_template

"""
create an object 'app' from the flask module
"""
app = Flask(__name__)

# set the routing to the main page
# 'route' decorator is used to access the root url
@app.route('/')
def index():
    name = "Muhammad"
    fruits = ['apple','orange','grapes']
    fruit = 'orange'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit)

# endpoints refer to the name of the view in an app
@app.route('/about')
def about():
    # list of images to pass to about.html
    images = ['mountain.jpg','instrument.jpg','stairs.jpg']
    return render_template('about.html', images = images)

@app.route('/quotes')
def quotes():
    return '<h1>Quotes</h1>'

# set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)