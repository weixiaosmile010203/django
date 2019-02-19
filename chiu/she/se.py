import re,requests,os

url = 'http://tv.bbs886.com/a/ar/Index.html'
urls_list = [
    'http://tv.bbs886.com/a/ar/Index_2.html'
    'http://tv.bbs886.com/a/ar/Index_3.html'
    'http://tv.bbs886.com/a/ar/Index_4.html'
    'http://tv.bbs886.com/a/ar/Index_5.html'
    'http://tv.bbs886.com/a/ar/Index_6.html'
]


response = requests.get(url)
page_regex = re.compile(r'href=(.*)target')
image_regex = re.compile(r'src="(.*)border')

for url in urls_list:
    urls = page_regex.findall(response.text)
#print(response.text)



#print(urls)

    url_list = []
for im in urls:
    if im.split('"')[1] not in url_list:
        url_list.append(im.split('"')[1])

#print(url_list)

    for page in url_list:
        #print(page)
        one_page_url = 'http://tv.bbs886.com' + page
        #print(one_page_url)
        index_page_name = one_page_url.split('/')[-1].split('.')[0]
        image_page = requests.get(one_page_url)
        image_url = image_regex.findall(image_page.text)
        os.mkdir(index_page_name)
        os.chdir('./' + index_page_name)
        for i in image_url:
            image = i.split('"')[0]
            #print(image)
            photo = requests.get(image)
            with open(image.split('/')[-1],'wb') as wb:
                wb.write(photo.content)
                wb.close()
            print('下载>>>>>'+image)
        os.chdir('../')


    #os.mkdir(one_page_url.endswith())

