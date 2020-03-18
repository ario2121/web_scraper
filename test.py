import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
import re

res = requests.get(url = 'https://divar.ir/v/%D8%AA%DB%8C%D8%A8%D8%A7-%D8%B5%D9%86%D8%AF%D9%88%D9%82-%D8%AF%D8%A7%D8%B1-%D9%85%D8%AF%D9%84-%DB%B9%DB%B4_%D8%B3%D9%88%D8%A7%D8%B1%DB%8C_%D8%AA%D9%87%D8%B1%D8%A7%D9%86_%D8%B3%D9%87%D8%B1%D9%88%D8%B1%D8%AF%DB%8C-%D8%B4%D9%85%D8%A7%D9%84%DB%8C_%D8%AF%DB%8C%D9%88%D8%A7%D8%B1/gXcR9Yia')
print(res)
soup = BeautifulSoup(res.content, 'lxml')
# print(soup.prettify())

# tree = ET.fromstring(soup)

f = soup.findAll('h1')
for i in f :
    print(i.find('class').text())
