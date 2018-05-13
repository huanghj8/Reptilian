# -*- coding: utf-8 -*-
from selenium import webdriver
#
# brower = webdriver.Chrome("Chromedriver")
# brower.get("https://www.baidu.com")
#
# print brower.page_source

# print webdriver.Chrome("Chromedriver").get("https://www.baidu.com")

# print webdriver.Chrome("Chromedriver").page_source

import urllib2


def get_Html(url):
    request_result = urllib2.Request(url)
    response_result = urllib2.urlopen(request_result)
    html = response_result.read()
    return html

# url = "https://www.baidu.com"
url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
print get_Html(url)

