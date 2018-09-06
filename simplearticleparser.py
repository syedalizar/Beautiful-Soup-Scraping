import requests
from bs4 import BeautifulSoup

with open('webpage.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
#print(soup.prettify()) if you want to view the pretty html

title = soup.title.text
print("Title: "+ title)

for article in soup.find_all('div', class_='article'):
    headline=article.h2.a.text


    print("")


    print(headline)

    summary = article.p.text

    print(summary)
