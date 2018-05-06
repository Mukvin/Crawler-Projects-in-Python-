# -*- coding: utf-8 -*-
from  bs4 import BeautifulSoup
import requests

#zzurl = 'http://zhuanzhuan.ganji.com/detail/967449936654598151z.shtml'
url = 'http://wh.ganji.com/diannao/33550626364097x.htm'
url1 = 'http://wh.ganji.com/diannao/33340112983108x.htm'

web_data = requests.get(url1)
soup = BeautifulSoup(web_data.text,'lxml')

# zzprices = soup.select('.price_now i')[0].text
# print(zzprices) #ok
#te = url.split('.')
#print(te)

# area = soup.select('.palce_li i')[0].text
# print(area) #ok

# price = soup.select('div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(1) > i')[0].text
#div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(1) > i
#div.leftBox > div:nth-child(2) > div > ul > li:nth-child(1) > i
# print(price) #ok

# pub_date = soup.select('.pr-5')[0].text.strip()
# print(pub_date) #ok

#div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(2) > a:nth-of-type(3)
area = soup.select('.det-infor > li  > a')[0].text + soup.select('.det-infor > li  > a')[-1].text
print(area)