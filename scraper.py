import requests
import time
from bs4 import BeautifulSoup

URL = 'http://www.imdb.com/title/tt0110912/reviews?start={0}'


f = open('reviews.txt', 'w')

for i in range(0, 50, 10):
    url = URL.format(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for e in soup.find(id="tn15content").find_all('p'):
        f.write(e.get_text().encode('utf-8'))
    time.sleep(1)

f.close()
