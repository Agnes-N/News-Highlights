import unittest
from models import sources,articles

Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('abc-news','ABC News','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com','https://abcnews.go.com/')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Gizmode.com','Jennings Brown','Man Claims He Invented Bitcoin, Is Ordered to Pay Billions in Bitcoin','A man who has insisted he is the man behind the pseudonymous identity of Satoshi Nakamoto, inventor of bitcoin, has been ordered to pay half of his cryptocurrency bounty to a man believed to be his former colleague','"https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816','"https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','2019-08-28T16:50:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))



if __name__ == '__main__':
    unittest.main()