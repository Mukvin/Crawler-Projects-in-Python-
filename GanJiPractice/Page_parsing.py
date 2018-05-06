# -*- coding: utf-8 -*-
from  bs4 import  BeautifulSoup
import  time
import requests
import pymongo
import random

client = pymongo.MongoClient('localhost',27017)
Ganji_info = client['Ganji']
url_list = Ganji_info['url_list']
item_info = Ganji_info['item_info']

headers  = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection':'keep-alive'
}

proxy_list = [
    'http://138.118.60.1:3128',
    'http://54.165.240.67:80',
    'http://58.62.84.114:9999',
    ]

proxy_ip = random.choice(proxy_list) # 随机获取代理ip
proxies = {'http': proxy_ip}

# spider 1
def get_links_from(channel, pages, who_sells='o'):
    # http://wh.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))
    #time.sleep(5)
    wb_data = requests.get(list_view, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    #print(soup)
    if soup.find('ul','pageLink clearfix'):
        for link in soup.select('td.t a '):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
            # return urls
    else:
        # It's the last page !
        pass

# spider 2
def get_item_info_from(url, data=None):
    wb_data = requests.get(url, headers=headers)
    if wb_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        if url.split('.')[0] == 'http://zhuanzhuan':
            data = {
                'title': soup.title.text.strip(),
                'price': soup.select('.price_now i')[0].text,
                'area': soup.select('.palce_li i')[0].text,
                ##wrapper > div.content.clearfix > div.leftBox > div:nth-child(2) > div > ul > li:nth-child(2) > a:nth-child(3)
                # 'cates': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
                'url': url
            }
            print(data)
            item_info.insert_one(data)
        else:

            data = {
            'title': soup.title.text.strip(),
            'price': soup.select('div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(1) > i')[0].text ,
            'pub_date':  soup.select('.pr-5')[0].text.strip() ,
            #'area': soup.select('.det-infor > li  > a')[0].text + soup.select('.det-infor > li  > a')[-1].text,
            'area': list(map(lambda  x : x.text ,soup.select('.det-infor > li  > a'))),
            ##wrapper > div.content.clearfix > div.leftBox > div:nth-child(2) > div > ul > li:nth-child(2) > a:nth-child(3)
            #'cates': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
            'url': url
            }
            print(data)
            item_info.insert_one(data)


#get_links_from('http://wh.ganji.com/diannao/',2)
#get_item_info_from('http://zhuanzhuan.ganji.com/detail/967449936654598151z.shtml')
#get_item_info_from('http://wh.ganji.com/diannao/33225402347840x.htm')