import urllib.request,json
from app import app
from datetime import datetime
from .models import sources,articles

Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["SOURCES_BASE_URL"]

def get_sources(category):
    '''
    function to get the json response to the url request
    '''
    get_sources_url = base_url.format(category,api_key)
    # print(get_sources_url)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results

def process_sources(sources_list):
    '''
    function that process the sources lists
    '''
    sources_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')

        sources_object = Sources(id, name, description, url, category)
        sources_results.append(sources_object)
        
    return sources_results

Articles = articles.Articles
article_url = app.config["ARTICLES_BASE_URL"]

def get_articles(id):
    '''
    function to get the json response to the url request
    '''
    get_articles_url = articles_url.format(id,api_key)
    # print(get_articles)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_results = json.loads(get_articles_data)

        articles_object = None
        if get_articles_response['articles']:
            articles_object_list = get_articles_results['articles']
            articles_object = process_articles(articles_object_list)

    return articles_object

def process_articles(articles_list):
	'''
    function that process the lists of articles
	'''
	articles_object = []
	for article in articles_list:
		id = article.get('id')
		author = article.get('author')
		title = article.get('title')
		description = article.get('description')
		url = article.get('url')
		urlToImage = article.get('urlToImage')
		publishedAt = article.get('publishedAt')
		
		if urlToImage:
			articles_results = Articles(id,author,title,description,url,urlToImage,publishedAt)
			articles_object.append(articles_results)	
		
	return articles_object
