# -*- coding: utf-8 -*-
from multiprocessing import Pool
from Page_parsing import get_item_info_from,url_list,item_info,get_links_from
from Chanel_extracting import chanel_list

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y

def get_all_links_from(channel):
     for i in range(1,100):
        get_links_from(channel,i)


if __name__ == '__main__':
    pool = Pool(processes=4)
    # pool = Pool()
    pool.map(get_all_links_from,chanel_list.split())
    pool.close()
