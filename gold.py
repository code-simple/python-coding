from bs4 import BeautifulSoup
import requests

gold = requests.get("https://www.cnbc.com/quotes/XAU=")
gold_soup = BeautifulSoup(gold.content,'lxml')
gold_price = gold_soup.select_one(".QuoteStrip-lastPrice").text.strip()

oil = requests.get("https://www.cnbc.com/quotes/@CL.1")
oil_soup = BeautifulSoup(oil.content,'lxml')
oil_price = oil_soup.select_one(".QuoteStrip-lastPrice").text.strip()

print("XAUUSD : "+gold_price+"\nUSLOIL : "+oil_price)
