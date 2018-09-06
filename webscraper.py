import requests
from bs4 import BeautifulSoup
import csv
source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('srapedata.csv', 'w')
csv_w = csv.writer(csv_file)
csv_w.writerow(['headers', 'text', 'youtube links'])
# print(soup.prettify())

for article in soup.find_all('article'):
    h = article.h2.a.text.encode('utf-8')
    print(h) #Headline
    s = article.find('div', class_='entry-content').p.text.encode('utf-8')
    print(s) #Article Text
    try:
        e_link=article.find('iframe', class_='youtube-player')['src'] #embedded link
        vid_id=e_link.split('/')[4] #extraction of youtube video id
        vid_id=vid_id.split('?')[0] #//

        l = ("https://youtube.com/watch?v="+vid_id).encode('utf-8')
        print(l)
    except Exception as e: #exception for cases wherer link is broken or not workable at least
        print None
     #link to video
    print(" ")

    csv_w.writerow([h, s, l])
csv_file.close()
