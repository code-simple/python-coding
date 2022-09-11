from bs4 import BeautifulSoup
import requests

webpage = requests.get("https://www.cnbc.com/quotes/XAU=")
soup = BeautifulSoup(webpage.content,'lxml')
price = soup.select_one(".QuoteStrip-lastPrice").text.strip()
print(price)