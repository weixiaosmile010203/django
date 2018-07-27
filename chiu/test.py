#!/usrbin/env python3
# coding: utf-8

import requests
import sys
import io
import re
import os


def get_pic(url):
    # 传入一个起始图片页面url，获取其他的所有图片页面url，如下：
    #<a href="http://www.mzitu.com/98966/2"><span>2</span></a>
    #    print ("获取页面url完成，开始获取图片url并下载...")
    q = requests.get(url, headers=head).text
    title_R = (r'<h2.*title">(.*)</h2>')
    title = re.findall(title_R, q)[0]
    page_R = (r'<span>(..)</span>')
    max_page = re.findall(page_R, q)[0]
    # title是网页标题，可能含有特殊字符，需过滤
    title = re.sub(u'[\/:*?">|< 满]+', "#", title)
    #title = re.sub(r'[.]+',"？",title)

    return (title, max_page)


def change_dir(where):
    try:
        os.chdir(where)
    except:
        os.mkdir(where)
        os.chdir(where)
        print("创建并切换到目录'" + where + "'完成")
#    print ("切换目录到'"+where+"'完成")


def down(one, url):
    # 传入一个包含图片的页面url，获取里面的图片地址并下载到本地，如下：
    #<img src="http://i.meizitu.net/2017/07/30a01.jpg" alt="**************">
    title = one[0]
    max_page = one[1]
    R = (r'<img src="(.*)" alt=".*>')
    change_dir('./mzitu')
    try:
        os.chdir("./" + title)
        print("'" + title + "'已下载，跳过")
        change_dir("../../")
    except:
        change_dir("./" + title)
        for i in range(0, int(max_page)):
            page = url + "/" + str(i + 1)
            html = requests.get(page, headers=head).text
            img_url = re.findall(R, html)[0]
            pic = requests.get(img_url, headers=head)
            with open(str(i) + '.jpg', 'wb') as f:
                for p in pic:
                    f.write(p)
        change_dir("../../")


def get_url_list(url):
    # 传入all页面的url，获取其他的所有文章链接，如下：
    #<a href="http://www.mzitu.com/99009" target="_blank">********</a>
    text = requests.get(url, headers=head).text
    R = (r'.*(http://www.mzitu.com/[0-9]+)".*')
#    print (text)
    print("从" + url + "获取专辑列表完成，开始获取页面url...")
    return re.findall(R, text)


if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
    # 曾经在运行时报字符编码错误所以添加了一条，但是现在去掉了，貌似也没报错。。。
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Referer': 'http://www.mzitu.com/37288/3'}
    url = 'http://www.mzitu.com/all'
    page_number = input("下载多少页？")
    #page_number = "2"
    print("#" + page_number + "#")
    url_list = get_url_list(url)
    count = 0
    for i in url_list:
        if str(count) < page_number:
            one = get_pic(i)
            down(one, i)
            count += 1
            print(i + "：已经全部下载完成")