
import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'http://jandan.net/pic/page-7707'
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
sorce_code = requests.get('http://jiandan.net/pic/page-7707',headers = header)
plain_text=sorce_code.text


Soup = BeautifulSoup(plain_text)
download_link = []
folder_path = '/user/renyongshuo/Desktop/a3/'
for pic_tag in Soup.find_all('img'):
    print(pic_tag)
    pic_link = pic_tag.get('src')
    download_link.append(pic_link)

for item in download_link:
    urllib.request.urlretrieve('http://jiqandan.net/'+item,folder_path + item[-10:])


