

import requests,re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
         }

url = 'http://www.win4000.com/wallpaper_detail_147096.html'

html = requests.get(url, header)
image_regex = re.compile(r'href=(.*)target')


print(html.text)
image_url_list = image_regex.findall(html.text)
for image in image_url_list:
    if ".jpg" in image:
        with open(image.split('/')[-1].split(".")[0]+".jpg", 'wb') as f:
            f.write(requests.get(image.split('"')[1], header).content)
            f.close()
            print('')