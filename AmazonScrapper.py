from bs4 import BeautifulSoup
import sys,requests,re,os
import pandas as pd


os.system('clear')

# Function to extract Product Title
def get_title(soup):

    try:
        title = soup.find("span", attrs={'id': 'productTitle'})
        title_value = title.string
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find(
            "span", attrs={'id': 'priceblock_ourprice'}).text.strip()
    except:
        try:
            # If there is some deal price
            price = soup.find('span', attrs={'id': 'priceblock_dealprice'}).text.strip()
        except:
            try:
                p1 = soup.find('span', attrs={'class': 'a-price-whole'}).text.strip()
                p2 = soup.find('span', attrs={'class': 'a-price-fraction'}).text.strip()
                price = str(p1+p2)
            except:
                try:
                    price = (soup.find('div', attrs={'id': 'usedBuySection'})).find_all('span')[1].text.strip()
                except:
                    try:
                        price = (soup.find('div', attrs={'class': 'a-section a-spacing-micro'})).find_all('span')[1].text.strip()
                    except:
                        price = ''

    return price

# Function to extract Brand
def get_brand(soup):
    try:
        brand = soup.find('a', attrs={'id': 'bylineInfo'}).string.strip()
    except:
        brand = ''
    return brand

# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find(
            "i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available

# Two arguments , first write link then file name with extension e.g Playstation4.csv
url =  str(sys.argv[1])
fileName = str(sys.argv[2])


# It find weather its US link ending with .com or Indian ending with .in 
# It's main purpose is to give correct homepage to Next button URL so it paginate 
# in correct country website
def checkURL(URL):
    domain = re.search('amazon(.*)/',URL)
    return str(f'https://www.amazon{domain.group(1)}')

def scrap(URL,fileName):
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US'})
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    print(f"\n\nPlease wait. I have to scrape data from {len(links)} Products \nProcessing URL: {URL} \n\n")
    # Test if banned/captcha
    # with open('test.html','w') as f:
    #     f.write(soup)

    #LISTS
    links_list = []
    products = []
    prices = []
    brands = []
    ratings = []
    reviews = []
    availble = []
    urls = []

    
    # Set correct domain 
    domain = checkURL(URL)

    # Next Button href 
    pagination = soup.find_all('a',attrs={'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
    for i in pagination: 
        next = domain+i['href']

    #Copy each link product link to List
    for link in links:
        links_list.append(link.get('href'))

    for link in links_list:
        new_webpage = requests.get(
            domain+link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "lxml")

        # add to list
        products.append(get_title(new_soup))
        prices.append(get_price(new_soup))
        brands.append(get_brand(new_soup))
        ratings.append(get_rating(new_soup))
        reviews.append(get_review_count(new_soup))
        availble.append(get_availability(new_soup))
        urls.append(str(domain+link))

    df = pd.DataFrame({'Title': products, 'Price': prices, 'Availability': availble,
                      'Brand': brands, 'Ratings': ratings, 'Product Ratings': reviews, 'URL': urls})
    df.to_csv(fileName, index=False,
              mode='a', encoding='utf-8')
    # Recursive Call
    scrap(next,fileName)

if __name__ == '__main__':
    scrap(url,fileName)