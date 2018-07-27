import requests
import re


url = ''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

image_html = requests.get('http://i.meizitu.net/2018/01/04c01.jpg',header)
print(image_html.content)
with open('水和岩石.jpg','wb') as p:
    p.write(image_html.content)

