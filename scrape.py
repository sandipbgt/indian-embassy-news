import requests
from lxml import html
from collections import OrderedDict

base_url = "http://www.indianembassy.org.np"
news_url = "http://www.indianembassy.org.np/index2.php?option=Ui3vzctxn5xHZVIBeyayl4Esp_mDrgNifomf1lhLMr4"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
           'Host': 'www.indianembassy.org.np'}

# to scrape articles from archive page
def scrape_news_archives():
    response = requests.get(news_url, headers=headers)
    tree = html.fromstring(response.content)
    archives = []

    for item in tree.xpath('//div[@id="press-release-lists"]/ul/li'):        
        article = OrderedDict([
            ('title', item.xpath('a/text()')[0]),
            ('url', '{0}/{1}'.format(base_url, item.xpath('a/@href')[0])),
            ('date', item.xpath('p[1]/text()')[0])])

        try:
            article['excerpt'] = item.xpath('p[2]/text()')[0].replace('\xa0', '')
        except IndexError:
            article['excerpt'] = ''

        archives.append(article)

    return archives

# to scrape articles from homepage
def scrape_news_articles():
    response = requests.get(base_url, headers=headers)
    tree = html.fromstring(response.content)
    articles = []

    for item in tree.xpath('//div[@id="press-release-holder"]/div[@class="press-releases"]'):        
        article = OrderedDict([
            ('title', item.xpath('h4/a/text()')[0].strip()),
            ('url', '{0}/{1}'.format(base_url, item.xpath('h4/a/@href')[0])),
            ('date', item.xpath('p[@class="date"]/text()')[0].strip())])

        try:
            article['excerpt'] = item.xpath('p[2]/text()')[0]
        except IndexError:
            article['excerpt'] = ''

        articles.append(article)

    return articles