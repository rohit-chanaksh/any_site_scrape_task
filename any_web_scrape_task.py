import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString

import pandas as pd

a_Url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

a_Header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

AResp = rq.get(url=a_Url, headers=a_Header)

# print(AResp.status_code)
# print('-------------------------------------------------------------------------------------------------------------------------')

bSoup = BeautifulSoup(AResp.content , 'html.parser')
# print(bSoup.prettify())

all_lap = bSoup.find_all('div' , attrs='product-wrapper card-body')
# print(all_lap[0].prettify())

print('Number of Laptops :-' , len(all_lap))

print('-------------------------------------------------------------------------------------------------------------------------')

# print(all_lap[0].find('div').find('h4').getText()) # Price
# print(all_lap[0].find('div').find('h4').next_sibling.next_sibling.find('a').attrs['title']) # Title
# print(all_lap[0].find('div').next_sibling.next_sibling.find('p').next_sibling.next_sibling.attrs['data-rating']) #Rating


def getTRP (lap) :
    T = lap.find('div').find('h4').next_sibling.next_sibling.find('a').attrs['title']
    R = lap.find('div').next_sibling.next_sibling.find('p').next_sibling.next_sibling.attrs['data-rating']
    P = lap.find('div').find('h4').getText()
    return {
        'Title' : T ,
        'Rating' : R ,
        'Price' : P
    }

laptop_data = [ getTRP(lap)  for lap in all_lap]

print(laptop_data)

lap_pd = pd.DataFrame(laptop_data)

lap_pd.to_csv('all laptop data.csv')
