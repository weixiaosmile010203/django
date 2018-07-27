import requests,re,os
from bs4 import BeautifulSoup
import time
#url = 'https://bcy.net/coser'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
         }
def download_image(url):
    response = requests.get(url,header).text
    # print(response)
    soup = BeautifulSoup(response,'lxml')
    a = soup.find_all('li')
    # print(a)
    image_page_regex = re.compile(r'href=\"(.*?)\"')
    raw_url_list = image_page_regex.findall(response)
    #/item/detail/6566561934160691459
    urls_regex = re.compile(r'(^\/item\/detail\/\w+)')
    # print(urls_regex.findall(raw_url_list))
    urls_list = []
    for i in raw_url_list:
        s = (urls_regex.findall(i))
        if s:
            urls_list.append('https://bcy.net'+s[0])
    #print(type(urls_list))
    #print(urls_list)

    for image_page_url in urls_list:
        #print(image_page_url)
        time.sleep(5)
        response = requests.get(image_page_url,header).text
        soup = BeautifulSoup(response,'lxml')
        dir_name = soup.title.string.split('|')[0]
        try:
            if os.path.exists(dir_name):
                print('%s已经存在，跳过',dir_name)
                continue
            else:
                os.mkdir(dir_name)
                os.chdir(dir_name)
        except:
            pass
            # os.mkdir(dir_name.split(':')[0].split('/')[0])
            # os.chdir(dir_name.split(':')[0].split('/')[0])
        else:
            #src="https://img9.bcyimg.com/user/508520/item/c0jgo/sup4g0zfjpkpkvw4kld7zpsk4fcptazr.jpg/w650"
            image_reges = re.compile(r'src="(https://.*?)\/\>')
            #print(response)
            raw_image_url = image_reges.findall(response)
            file_name = 1
            print('正在下载>>', dir_name)
            for i in raw_image_url:
                if 'w650' in i:
                    image_url = i.split('"')[0].split('/w650')[0]
                    response = requests.get(image_url, header).content
                    with open(str(file_name)+'.jpg', 'wb')as rc:
                        rc.write(response)
                    rc.close()
                    print('已经下载>>>',file_name)
                    file_name += 1

            os.chdir('../')
            print('当前页下载完成，退出目录')




urls = ['https://bcy.net/circle/timeline/showtag?since=25061.502&grid_type=flow&sort=hot&tag_id=399'
'https://bcy.net/circle/timeline/showtag?since=25061.462&grid_type=flow&sort=hot&tag_id=399'
'https://bcy.net/circle/timeline/showtag?since=25061.405&grid_type=flow&sort=hot&tag_id=399']


for url in urls:
    download_image(url)