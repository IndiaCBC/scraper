#!/usr/bin/env python
"""Script to fetch coffee data from Bluetokai"""
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def coffee_data():
    """Get Coffee Details"""
    site = 'https://bluetokaicoffee.com'
    url = site + '/collections/coffee'
    coffees = []
    req = requests.get(url)
    if req.ok:
        soup = BeautifulSoup(req.text, "html.parser")
        coffee_list = soup.find(attrs={'id': 'shop-products'}).\
                findAll('div', attrs={'class': 'col'})
        for coffee_div in coffee_list:
            coffee = {}
            coffee_details = coffee_div.find('div', attrs={'class': 'details'})

            coffee['images'] = coffee_div.find('img')['src']
            coffee['name'] = coffee_details.find(attrs={'class': 'pd-name'}).text
            coffee['price'] = coffee_details.find(attrs={'class': 'pd-price'}).text
            coffee['notes'] = coffee_details.find(attrs={'class': 'roast-lab'}).text.strip()
            coffee['roast'] = coffee_details.find(attrs={'class': 'roast-lab2'}).text.strip()
            coffee['link'] = site + coffee_div.find('a')['href']
            coffees.append(coffee)
        pprint(coffees)


if __name__ == "__main__":
    coffee_data()
