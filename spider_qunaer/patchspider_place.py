import os
import time
import random
import spider_test1 as st


def patch_spider_place(keyword):
    """
    批量爬取去哪儿景点
    :param keyword:
    :return:
    """
    # 写入数据前先清空之前的数据
    # if os.path.exists()
    # 批量爬取
    pageSize = 1
    while pageSize != -1:
        json = st.spider_place(keyword, pageSize)
        list = json['data']['sightList']
        print(list)
        pageSize = pageSize + 1
        if len(list) < 15:
            pageSize = -1
        time.sleep(random.randint(2, 5))

    print("爬取完成！")


patch_spider_place('国庆旅游景点')
