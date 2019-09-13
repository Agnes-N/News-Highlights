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
    from source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')

        sources_object = Sources(id, name, description, url)
        sources_results.append(sources_object)

def get_articles(id):
     '''
    function to get the json response to the url request
    '''
    get_articles_url = article_url(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_results = json.loads(get_articles_data)

        articles_object = None
        if get_articles_response['articles']:
            articles_object_list = get_articles_results['articles']
            articles_object = process_results(articles_object_list)

    return articles_object

def process_articles(articles_list):
	'''
	'''
	articles_object = []
	for article in articles_list:
		id = article.get('id')
		author = article.get('author')
		title = article.get('title')
		description = article.get('description')
		url = article.get('url')
		image = article.get('urlToImage')
		date = article.get('publishedAt')
		
		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	
		

		

		

	return articles_object
