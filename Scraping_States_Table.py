# -*- coding: utf-8 -*-
"""
https://en.wikipedia.org/wiki/States_and_union_territories_of_India
"""

wiki = "https://en.wikipedia.org/wiki/States_and_union_territories_of_India"

import requests

from bs4 import BeautifulSoup

source = requests.get(wiki).text

soup = BeautifulSoup(source,"lxml")
#we want to read table data
#SOUP to READ TABLE DATA ONLY

table_data = soup.find('table', class_ = 'wikitable')

import pandas as pd

df=pd.read_html(str(table_data))
# convert list to dataframe
df=pd.DataFrame(df[0])
df.head()

df.to_csv('States_Table.csv', index=False)
