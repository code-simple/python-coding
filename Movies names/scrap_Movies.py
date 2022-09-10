from bs4 import BeautifulSoup
import requests

web = requests.get('https://lookmovie2.to/page/1')
soup = BeautifulSoup(web.content, 'lxml')

titles = soup.select('div>.mv-item-infor')
for index, i in enumerate(titles):
    print(str(index)+" - "+i.text.strip())
