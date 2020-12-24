import random
import urllib.request
import requests

from bs4 import BeautifulSoup


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name) 

def entity_table_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://dev1.datasense.host/Entity/ViewTable/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.find_all('tr', {'class': 'k-master-row'}):
            table_row = link.find('td').contents
            print(str(table_row))


entity_table_spider(2)
