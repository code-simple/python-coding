# Script to Scrap all Titles and URLS of https://lookmovie2.to 
from bs4 import BeautifulSoup
import requests, pandas as pd

webpage = "https://lookmovie2.to/page/1"

def scrap(URL):
    web = requests.get(URL)
    soup = BeautifulSoup(web.content, 'lxml')

    titles = []
    urls = []

    nextpage = ("https:"+soup.select_one(".pagination_next")["href"])
    
    title = soup.select("div>.mv-item-infor")

    print("Working : ?",(URL,))
    
    for  i in title:
        titles.append(i.text.strip())
        urls.append("https://lookmovie2.to"+i.find("a")["href"])

    df = pd.DataFrame({'Title': titles,'URL': urls})
    df.to_csv('lookmovie.csv', index=False, mode='a', encoding='utf-8')
    
    scrap(nextpage)

if __name__ == '__main__':
    scrap(webpage)