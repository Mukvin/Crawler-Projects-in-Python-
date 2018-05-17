
from  bs4 import  BeautifulSoup
import requests
import time
import urllib.request

base_url = 'https://weheartit.com/inspirations/taylorswift?page={}&before=258728622'
path = 'F://Desktop/MM/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}
proxies = {"http": "http://121.69.29.162:8118"}
# 此网站会有针对 ip 的反爬取，可以采用代理的方式

def get_img_url(num):
    img_urls= []
    for page_num in range(1,num + 1):
        full_url = base_url.format(page_num)
        web_data = requests.get(full_url,proxies = proxies)
        soup = BeautifulSoup(web_data.text , 'lxml')
        images = soup .select('img.entry-thumbnail')

        for i in images :
            img_urls.append(i.get('src'))

    #print((len(img_urls)),'images shall be download !')
    return img_urls


#print(get_img_url(1))
#'https://data.whicdn.com/images/285757002/superthumb.jpg'
def dl_img(url):
    time.sleep(2)
    urllib.request.urlretrieve(url , path + url.split('/')[-2] +url.split('/')[-1])
    #print('Done')
    #升级进度显示

print((len(get_img_url(1))),'images shall be download !')
length = len(get_img_url(1))
i = 1
for url in get_img_url(1):
    dl_img(url)
    if i <= length:
        print(str(round(i /length,3) * 100) + '% Done !')
        i = i + 1