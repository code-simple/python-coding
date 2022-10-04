# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def goldPrice():
    options = Options()
    options.headless = True  # hide GUI
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=options)
    content = driver.get("https://www.tradingview.com/symbols/XAUUSD/")
    price = driver.find_element(By.CLASS_NAME, "tv-symbol-price-quote__value").text.strip()
    # soup = BeautifulSoup(driver.page_source,'lxml')
    # price = soup.select_one(".tv-symbol-price-quote__value").text.strip()
    driver.close()
    return price

def oilPrice():
    options = Options()
    options.headless = True  # hide GUI
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=options)
    content = driver.get("https://www.tradingview.com/symbols/FX-USOILSPOT/")
    price = driver.find_element(By.CLASS_NAME, "tv-symbol-price-quote__value").text.strip()
    # soup = BeautifulSoup(driver.page_source,'lxml')
    # price = soup.select_one(".tv-symbol-price-quote__value").text.strip()
    driver.close()
    return price


if __name__ == "__main__":
    print(goldPrice()+"   "+oilPrice())