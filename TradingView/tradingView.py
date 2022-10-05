from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def price(instrument):
    options = Options()
    options.headless = True  # hide GUI
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s,options=options)
    content = driver.get("https://www.tradingview.com/symbols/"+instrument)
    price = driver.find_element(By.CLASS_NAME, "tv-symbol-price-quote__value").text.strip()
    driver.close()
    return price

if __name__ == "__main__":
    print(price("XAUUSD"),price("FX-USOILSPOT"))