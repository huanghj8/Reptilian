#!/usr/bin/env python
# -*- coding: utf-8 -*-
import expanddouban


# 任務1：定義getMovieUrl函數，參數為分類和地區，輸出對應的url
def getMovieUrl(category="剧情", location="剧情"):
    root_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    url = root_url + ',' + category + ',' + location
    return url


# 任務2：根據URL獲取對應電影頁面HTML

html = expanddouban.getHtml(getMovieUrl(), loadmore=True, waittime=2)
print html