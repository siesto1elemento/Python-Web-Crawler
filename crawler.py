import requests
from bs4 import BeautifulSoup

url_ = ['https://www.scrapingcourse.com/ecommerce/']

request_url = url_.pop()

visited_url = []
visited_url.append(request_url)

r = requests.get(request_url)
html_ = r.content

soup = BeautifulSoup(html_, 'html.parser')
link_elements = soup.select("a[href]")



for link_element in link_elements:
    url = link_element['href']
    if "https://www.scrapingcourse.com/ecommerce/" in url:
        if url not in visited_url and url not in url_:
            url_.append(url)

print(url_)













