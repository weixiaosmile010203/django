from bs4 import BeautifulSoup
import requests,os

url = 'https://bcy.net/coser'
response = requests.get(url)

soup = BeautifulSoup(response.text,'lxml')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print('---------------------------')
# print('head》》',soup.head)
imgs = soup.find_all('img')
print(imgs)
for im in imgs:
    print(im.get('src'))
