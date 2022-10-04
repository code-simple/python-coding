from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def goldPrice():
    options = Options()
    options.headless = True  # hide GUI
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=options)
    content = driver.get("https://www.tradingview.com/symbols/XAUUSD/")
    soup = BeautifulSoup(driver.page_source,'lxml')
    price = soup.select_one(".tv-symbol-price-quote__value").text.strip()
    driver.close()
    return price

def oilPrice():
    options = Options()
    options.headless = True  # hide GUI
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=options)
    content = driver.get("https://www.tradingview.com/symbols/USOIL/")
    soup = BeautifulSoup(driver.page_source,'lxml')
    price = soup.select_one(".tv-symbol-price-quote__value").text.strip()
    driver.close()
    return price


if __name__ == "__main__":
    print(goldPrice()+"   "+oilPrice())