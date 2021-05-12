#!/usr/bin/env python
"""Script to fetch coffee data from Bluetokai"""
from pprint import pprint
from bs4 import BeautifulSoup
import requests

def coffee_data():
    """Get Coffee Details"""
    site = 'https://curiouslifecoffee.com'
    url = site + '/shop'
    coffees = []
    req = requests.get(url)
    if req.ok:
        soup = BeautifulSoup(req.text, "html.parser")
        product_list = soup.find(attrs={'class': 'productSubsEntryBox'})\
                .findAll(attrs={'class':'productSubsEntry'})
        for coffee_section in product_list:
            coffee_roast = coffee_section.find('div').text
            section_type = coffee_section.attrs['id']
            for coffee_list in coffee_section.find('ul'):
                if section_type != 'gear':
                    if coffee_list != '\n':
                        coffee = {}
                        coffee['images'] = coffee_list.find('img')['src']
                        coffee['name'] = coffee_list.find('strong',\
                                attrs={'class': 'product-title'}).text
                        coffee['price'] = coffee_list.find('span',\
                                attrs={'class': 'product-price'}).text
                        coffee['notes'] = str(coffee_list.find('div',\
                                attrs={'class': 'hover-description'}).\
                                text.strip().split('\n')[:-1])
                        coffee['roast'] = coffee_roast
                        coffee['link'] = coffee_list.find('a')['href']
                        coffees.append(coffee)
        pprint(coffees)


if __name__ == "__main__":
    coffee_data()
