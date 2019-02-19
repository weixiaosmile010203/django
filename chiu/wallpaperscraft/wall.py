import re,requests,os

#url = 'https://wallpaperscraft.com/all/1920x1080'
def download(url):
    response = requests.get(url).text
    #创建正则表达式
    page_regex = re.compile(r'src="(https:.*?\.jpg)')
    #获取一页图片的url
    one_page_url = page_regex.findall(response)
    # print(one_page_url)
    for i in one_page_url:
        image_url = i.split('300x168.jpg')[0]+'1920x1080.jpg'
        image_name = i.split('/')[4].split('_300x168.jpg')[0] + '.jpg'
        image = requests.get(image_url).content
        if os.path.exists(image_name):
            print('(%s)已经存在，跳过' % image_name)
            continue
        else:
            with open(image_name, 'wb') as fb:
                fb.write(image)
            fb.close()
            print('已经下载>>>>>>>>(%s)' % image_name)

def urls():
    urls = []
    url = 'https://wallpaperscraft.com/all/1920x1080'
    num = int(input('请输入下载页数:'))
    for i in range(243, num):
        urls.append(url + '/page' + str(i+1))
    return urls

for i in urls():
    print('下载>>>>>>>>>>%s' %i)
    download(i)


