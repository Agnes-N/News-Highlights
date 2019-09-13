from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    title = 'Home -Welcome to the best news online'
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    view function that returns the news details page and its data
    '''
    render_template('movie.html', id = news_id)