import re
import requests
import os


url = 'http://www.win4000.com/zt/haishui.html'

def index_page():
    html = requests.get('http://www.win4000.com/zt/haishui.html')
    #print(html.text)
    image_url = re.compile(r'href=(.*)alt')
    page_list = image_url.findall(html.text)
    #获取列表
    return page_list

def jiexi_url(urls):
    image_list = []
    for image in urls:
        image = image.split('"')[1]
        #print(image)
        image_list.append(image)
    return image_list
    #print(urls)

def download(url, index):
    image_html = requests.get(url)
    #print(image_html.text)
    name_regex = re.compile(r'alt=(.*)title')
    name = name_regex.findall(image_html.text)[0].split('"')[1]


    image_regex = re.compile(r'class="pic-large"(.*)alt')
    image_html = image_regex.findall(image_html.text)[0].split('"')[1]
    photo = requests.get(image_html)
    with open(name+"_"+str(index)+".jpg", 'wb') as p:
        p.write(photo.content)
        p.close()


def resive(url):

    test  = requests.get(url).text
    num_regex = re.compile(r'<em>(\w+)</em>')
    num = int(num_regex.findall(test)[0])

    for i in range(num):
        if i == 0:
            pass
        else:
            pos = url.split('_')
            inde = pos[-1].split('.')[0]+'_'+str(i+1)
            newurl = 'http://www.win4000.com/wallpaper_detail_' + inde + '.html'
            print(newurl)
            download(newurl, num)
            return newurl







urls = index_page()
img = jiexi_url(urls)
# print(img[0])
for i in range(len(img)):
    print(img[i])
    download(img[i], i)
    print(img[i]+"--------finish")
    print("*"*90)
    resive(img[i])
