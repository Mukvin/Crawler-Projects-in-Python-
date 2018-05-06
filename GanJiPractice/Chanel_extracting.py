# -*- coding: utf-8 -*-
from  bs4 import BeautifulSoup
import requests

start_url = 'http://wh.ganji.com/wu/'
url_host= 'http://wh.ganji.com' #结果多了一条斜杠，所以在这里最后末尾去掉下 例如#http://wh.ganji.com//jiaju/

def get_index_url( url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text,'lxml')
    links = soup.select('.fenlei > dt > a')
    #print( links)
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)


get_index_url(start_url)

chanel_list = '''
http://wh.ganji.com/jiaju/
http://wh.ganji.com/rirongbaihuo/
http://wh.ganji.com/shouji/
http://wh.ganji.com/bangong/
http://wh.ganji.com/nongyongpin/
http://wh.ganji.com/jiadian/
http://wh.ganji.com/ershoubijibendiannao/
http://wh.ganji.com/ruanjiantushu/
http://wh.ganji.com/yingyouyunfu/
http://wh.ganji.com/diannao/
http://wh.ganji.com/xianzhilipin/
http://wh.ganji.com/fushixiaobaxuemao/
http://wh.ganji.com/meironghuazhuang/
http://wh.ganji.com/shuma/
http://wh.ganji.com/laonianyongpin/
http://wh.ganji.com/xuniwupin/
http://wh.ganji.com/qitawupin/
http://wh.ganji.com/ershoufree/
http://wh.ganji.com/wupinjiaohuan/
'''