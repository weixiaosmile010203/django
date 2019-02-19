import re
import requests
import os


#url = 'http://www.mzitu.com/114805/'
num = 1
# for page in range(58):
#     if page == 1

head = {'Referer': 'http://www.mzitu.com/114805/58',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

while num < 60:
    url = 'http://www.mzitu.com/114805/'
    url = url + str(num)
    num += 1
    response = requests.get(url).text
    image_url = re.findall(r'img src="(.*?\.jpg)"', response)
    image_name = re.findall(r'main-title">(.*?)</h2>', response)
    image = requests.get(image_url[0],head)
    print(image_url[0])
    #print(image.content)

    # with open(image_name[0] + ".jpg",'wb') as wb:
    #     wb.write(image.content)
    # wb.close()
    #
    # print(url,'>>>>>>>>>已经下载。保存为>>>',image_name)



# response = requests.get(url)
# image_url = re.findall(r'img src="(.*?\.jpg)"',response.text)
# image_name = re.findall(r'main-title">(.*?)</h2>',response.text)
#
#
# print(image_name[0])
# print(image_url)