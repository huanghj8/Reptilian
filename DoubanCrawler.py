# -*- coding: utf-8 -*-
import codecs
import csv
import sys

from bs4 import BeautifulSoup

import expanddouban

reload(sys)
sys.setdefaultencoding('utf-8')


# 任務1：定義getMovieUrl函數，參數為分類和地區，輸出對應的url
def get_movie_url(category='剧情', location='美国'):
    root_url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影'
    url = root_url + ',' + category + ',' + location
    return url


# 任務2：根據URL獲取對應電影頁面HTML
# html = expanddouban.getHtml(getMovieUrl(), loadmore=False, waittime=2)


def get_html(category, location):
    html = expanddouban.getHtml(get_movie_url(category, location), loadmore=False, waittime=1)
    return html


# 任務3：定義電影類
class Movie:
    def __init__(self, name, rate, location, category, info_link, cover_link):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link

    def print_movie(self):
        return "{},{},{},{},{},{}".format(self.name, self.rate, self.location, self.category, self.info_link,
                                          self.cover_link)


# 任務4：定義getMovies函數，參數為類型和地區，輸出對應的電影信息列表
def get_movies(category, location_list):
    movies = []
    for location in location_list:
        soup = BeautifulSoup(get_html(category, location), 'html.parser')
        content_a = soup.find(id='content').find(class_='list-wp').find_all('a', recursive=False)
        for element in content_a:
            m_name = element.find(class_='title').string
            m_rate = element.find(class_='rate').string
            m_location = location
            m_category = category
            m_info_link = element.get('href')
            m_cover_link = element.find('img').get('src')
            movies.append(Movie(m_name, m_rate, m_location, m_category, m_info_link, m_cover_link).print_movie())
    return movies


# 任務5：選擇三個電影類型，獲取所有電影信息，輸出到文件movies.csv
category_list = ['武侠', '灾难', '西部']
# location_list = ['中国大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '德国', '意大利', '西班牙',
#  '印度', '泰国', '俄罗斯', '伊朗', '加拿大','澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']
location_list = ['美国']
my_list1 = get_movies('剧情', location_list)

# my_list1 = getMovies('武侠', location_list)
my_list2 = get_movies('战争', location_list)
my_list3 = get_movies('爱情', location_list)

f = codecs.open('movies.csv', 'w', 'utf_8_sig')
writer = csv.writer(f)
writer.writerow(my_list1)
writer.writerow(my_list2)
writer.writerow(my_list3)
f.close()


# # 任務6：將每個電影類別按地區電影數量排序，前三名的地區是哪些，佔比多少，結果輸出到文件output.txt
# def putMax(mylist, location = ""):
#     input_dict = {'中国大陆': 0, '美国': 0, '香港': 0, '台湾': 0, '日本': 0, '韩国': 0, '英国': 0, '法国': 0,
# '德国': 0, '意大利': 0, '西班牙': 0,
# '印度': 0, '泰国': 0, '俄罗斯': 0, '伊朗': 0, '加拿大': 0, '澳大利亚': 0, '爱尔兰': 0, '瑞典': 0, '巴西': 0, '丹麦': 0}
#     total = 0
#     for movie in mylist:
#         if location in movie:
#             input_dict[location] += 1
#             total += 1
#     for idict in input_dict:
#         while total > 0:
#             input_dict[idict] = round((input_dict[idict] / total) * 100, 2)
#     return sorted(input_dict.items(), key=lambda x: x[1], reverse=True)[:3]
#
#
# def turnTostr(max_tuple):
#     result_list = []
#     i = 0
#     while i < len(max_tuple):
#         element = max_tuple[i]
#         ele = str(element)
#         e = "{}占百分之{},排名第{}".format(ele[2:ele.index(',') - 1], ele[ele.index(',') + 2: -3], i + 1)
#         i += 1
#         result_list.append(e)
#     return result_list
#
#
# max_list = [turnTostr(putMax(my_list1)), turnTostr(putMax(my_list2)), turnTostr(putMax(my_list3))]
#
# f = open('output.txt', 'w')
# f.write("我選擇電影類型為科幻、歌舞和歷史。\n")
# j = 0
# while j < len(category_list):
#     f.write("{}類型電影數量排名前三的地區和百分比為：\n".format(category_list[j]))
#     i = 0
#     while i < len(max_list[j]):
#         f.write(max_list[j][i])
#         f.write('\n')
#         i += 1
#     j += 1
# f.close()
