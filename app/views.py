from flask import render_template
from app import app
from .request import get_sources,get_source

#views
@app.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')

    message = 'Welcome to the best news Highlights'
    title = 'Home'
    return render_template('index.html',title = title,message = message,business_sources = business_sources,sports_sources = sports_sources,technology_sources= technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<int:id>')
def articles(id):
    '''
    view function that returns the news details page and its data
    '''
    sources = get_source(id)
    title = f'{sources.title}'
    render_template('articles.html',title = title,sources = sources)