from app import app
import urllib.request,json
from models import sources,articles

Sources = sources.Sources
Articles = articles.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["SOURCES_BASE_URL"]
article_url = app.config["ARTICLES_BASE_URL"]

def get_sources(category):
    '''
    function to get the json response to the url request
    '''
    get_sources_url = base_url(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None
        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            source_results = process_results(source_results_list)

    return source_results
    # get_articles_url = article_url(category,article_url)