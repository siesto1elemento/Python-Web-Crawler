import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapingcourse.com/ecommerce/'

r = requests.get(url)
html_ = r.content

soup = BeautifulSoup(html_, 'html.parser')
link_elements = soup.select("a[href]")


urls = []
for link_element in link_elements:
    url = link_element['href']
    if "https://www.scrapingcourse.com/ecommerce/" in url:
        urls.append(url)













