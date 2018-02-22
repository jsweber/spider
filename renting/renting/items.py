# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RentingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#安居客
#https://sh.zu.anjuke.com/?pi=baidu-cpchz-sh-hexin1&kwid=63651556880&utm_term=%E7%A7%9F%E6%88%BF
class AnjukeItem(scrapy.Item):
    pass

#链家
#https://sh.lianjia.com/zufang/
class LianjiaItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    living_space = scrapy.Field()#租住面积
    rent_price = scrapy.Field()#价格
    unit = scrapy.Field() #元/月
    house_type = scrapy.Field() #户型
    floor = scrapy.Field() #楼层
    orientation = scrapy.Field() #朝向
    community = scrapy.Field()#小区
    location = scrapy.Field() #位置
    publish_time = scrapy.Field()#租房发布时间
    phone = scrapy.Field()#联系方式
    crawling_time = scrapy.Field()#爬取时间
    

