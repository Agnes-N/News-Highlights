from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    message = 'Welcome to the best news Highlights'
    title = 'Home'
    return render_template('index.html', title = title,message = message)

@app.route('/sources/<int:id>')
def articles(id):
    '''
    view function that returns the news details page and its data
    '''
    render_template('articles.html', id = id)