import re
import requests
import csv
from requests import exceptions
import codecs
import time
#定义爬取函数，返回网页源代码
def download_page(url, para=None):
    time.sleep(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    try:
        if para:
            response = requests.get(url, params=para, headers=headers,timeout=10)
        else:
            response = requests.get(url, headers=headers,timeout=10)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            return response.text
        else:
            return None
    except exceptions.Timeout as e:
        print("出错")
        return None
    except exceptions.HTTPError as e:
        print("出错")
        return None
#生成网址列表
url_s = []
for i in range(1, 1000):
    url = "http://guba.eastmoney.com/list,600559_" + str(i) + ".html"
    url_s.append(url)
print("网页链接已经生成")
comments = []
i=1
for c in url_s:
    html = []
    s = download_page(c)
    print(i)
    i=i+1
    if(s!=None):
        pattern = r"""(<div class="articleh.*?>.*?<span class="l5 a5">.*?</span>)"""
        comment = re.findall(pattern, s, re.S)
        comments.append(comment)
print(len(comments))

# In[5]:
titles = []
dates = []
read_number = []
reply_number = []
hangye = []
fenge=[]
read_pattern = r"""<span class="l1 a1">(.*?)</span>"""
reply_pattern = r"""<span class="l2 a2">(.*?)</span>"""
title_pattern = r"""<span class="l3 a3"><a href=".*?title="(.*?)">"""
date_pattern = r"""<span class="l5 a5">(.*?)</span>"""
for i in comments:
    for c in i:
        t = re.findall(title_pattern, c)
        if len(t) > 0:
            titles.append(t[0])
            fenge.append('&&&')
            d = re.findall(date_pattern, c)
            if len(d) > 0:
                dates.append(d[0])
            else:
                dates.append(0)
            n = re.findall(reply_pattern, c)
            if len(n) > 0:
                reply_number.append(n[0])
            else:
                reply_number.append(0)
            e = re.findall(read_pattern, c)
            if len(e) > 0:
                read_number.append(e[0])
            else:
                read_number.append(0)
from pandas.core.frame import DataFrame
temp={
    "read_number" : read_number,
    "fenge1":fenge,
    "reply_number" : reply_number,
    "fenge2":fenge,
    "titles":titles,
    "fenge3":fenge,
    "dates":dates
   }
data=DataFrame(temp)#将字典转换成为数据框
data=data.drop(data[data.titles==''].index)
print(data)
data.to_csv("data-1.csv",encoding="utf-8")