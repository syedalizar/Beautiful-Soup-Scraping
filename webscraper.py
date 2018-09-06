import requests
from bs4 import BeautifulSoup

source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

for article in soup.find_all('article'):
    print(article.h2.a.text) #Headline
    print(article.find('div', class_='entry-content').p.text) #Article Text
    try:
        e_link=article.find('iframe', class_='youtube-player')['src'] #embedded link
        vid_id=e_link.split('/')[4] #extraction of youtube video id
        vid_id=vid_id.split('?')[0] #//

        print("https://youtube.com/watch?v="+vid_id)
    except Exception as e: #exception for cases wherer link is broken or not workable at least
        print None
     #link to video
    print(" ")
