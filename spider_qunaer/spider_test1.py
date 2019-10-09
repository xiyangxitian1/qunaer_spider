import requests
import os
import numpy as np
import pandas as pd


def spider_place(keyword, page):
    """
    爬取景点
    :param keyword:  搜索关键字
    :param page:  分页参数
    :return:
    """
    url = f'https://piao.qunar.com/ticket/list.json?from=mps_search_suggest_h&keyword=' \
          f'{keyword}&page={page}'

    headers = {
        'accept': 'application / json, text / javascript, * / *; q = 0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'piao.qunar.com',
        'Referer': 'https://piao.qunar.com/ticket/list_%E5%9B%BD%E5%BA%86%E6%97%85%E6%B8%B8%E6%99%AF%E7%82%B9.html?from=mps_search_suggest_h&keyword=%E5%9B%BD%E5%BA%86%E6%97%85%E6%B8%B8%E6%99%AF%E7%82%B9&page=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    return response.json()


PLACE_EXCEL_PATH = ""


def save_excel(place_list):
    """
    将json数据生成excel
    :param place_list: 景点数据
    :return:
    """
    # pandas对excel没有追加模式，只能先读后写

    if os.path.exists(PLACE_EXCEL_PATH):
        pass


json = spider_place('国庆旅游景点', 1)
list = json['data']['sightList']

for v in list:
    print(v)
print(len(list))
