from bs4 import BeautifulSoup
import requests
import time
from fuzzywuzzy import fuzz
import pandas as pd


def is_similar(search, title):
    return fuzz.partial_ratio(search, title) >= 71


def find_listings(search):
    results = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.amazon.com/",
    "Connection": "keep-alive",}
    URL = f"https://www.amazon.com/s?k={search.replace(' ','+')}"
    html_text = requests.get(f'{URL}', headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    listings = soup.find_all('div', {'data-component-type': 's-search-result'})
    for listing in listings:
        title = listing.find('h2').a.span.text
        price = listing.find('span', class_='a-price')
        star = listing.find('span', class_="a-icon-alt").text.split()[0]
        if price is not None:
            price = price.span.text
        else:
            price = 'N/A'
        if is_similar(search, title):
            results.append([title,price,star])
            data_frame = pd.DataFrame(results, columns=['Title', 'Price', 'Rating out of 5'])
    data_frame.to_csv('results.csv')

search = input('What do you want to search? \n')

find_listings(search)