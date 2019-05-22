import requests
from requests.exceptions import RequestException
import random
import re
import time
import pandas as pd
from bs4 import BeautifulSoup

region_url = ['jiangning', 'xuanwuqu', 'gulouqu', 'jianye', 'qinhuai',
              'yuhuatai', 'pukouqu', 'qixiaqu', 'liuhequ', 'lishuixian']
region_name = ['江宁区', '玄武区', '鼓楼区', '建邺区', '秦淮区',
               '雨花台区', '浦口区', '栖霞区', '六合区', '溧水区']


# 重新爬取数据，分南京各个区进行爬取，保存
def write_to_file(content):
    with open('{}二手房房价信息.csv'.format(region_name[m]), 'a', encoding='utf-8-sig') as f:
        f.write(str(content) + '\n')


def get_one_page(url):
    try:
        user_agent =\
            [  # User Agent 用户代理，它是一个特殊字符串头，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等
            'Mozilla/5.0 (Windows NT 10.0; WOW64)', 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
            'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
            'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
            'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11'
            ]
        # 破解反扒的措施，利用代码伪装成浏览器 访问浏览器
        header = {"User-Agent": random.choice(user_agent),}
        response = requests.get(url, headers=header)

        if response.status_code == 200:  # 状态码 200 为正常
            return response.text  # 返回网页html代码
        return None
    except RequestException:
        return None


# 解析一页的HTML代码
def parse_one_page(html):
    pattern = re.compile('<li.*?<div class="pic">.*?</div>.*?<div class="list-info">.*?<h2 class=.*?'
                         '<a.*?target=.*?>(.*?)&nbsp.*?</h2>.*?<p class=.*?<span>(.*?)室(.*?)厅(.*?)卫'
                         '.*?<span>(.*?)㎡.*?<span>.*?</span>.*?<span>.*?</span>.*?</p>.*?<p class.*?'
                         'target=.*?>(.*?)</a>.*?href=.*?target=.*?>(.*?)</a>.*?<a>(.*?)</a>.*?</p>.*?'
                         '<div class=\'price\'>.*?<p class.*?<b>(.*?)</b>.*?</li>', re.S)  # re.S用来匹配换行符
    items = re.findall(pattern, html)
    for item in items:
        item = list(item)
        # print(item)
        s = ''
        for j in range(len(item) - 1):
            item[j] = item[j].replace('，', '')
            item[j] = item[j].replace(',', '')
            if j == 5:
                s += item[8] + ','
                s += item[j] + ','
            else:
                s += item[j] + ','
        if len(s) <= 80:
            print(s)
            # write_to_file(s)


def main(page):
    url = 'https://nj.58.com/{}/ershoufang/pn'.format(region_url[m]) + str(page) + '/'
    # https://nj.58.com/jiangning/ershoufang/pn2/   江宁区
    # https://nj.58.com/xuanwuqu/ershoufang/pn2/    玄武区
    # https://nj.58.com/gulouqu/ershoufang/pn2/     鼓楼区
    # https://nj.58.com/jianye/ershoufang/pn2/      建邺区
    # https://nj.58.com/qinhuai/ershoufang/pn2/     秦淮区
    # https://nj.58.com/yuhuatai/ershoufang/pn2/    雨花台
    # https://nj.58.com/pukouqu/ershoufang/pn2/     浦口区
    # https://nj.58.com/qixiaqu/ershoufang/pn2/     栖霞区
    # https://nj.58.com/liuhequ/ershoufang/pn2/     六合区
    # https://nj.58.com/lishuixian/ershoufang/pn2/  溧水区
    # 高淳只有33页，其他都是70页
    html = get_one_page(url)
    parse_one_page(html)


# 启动主函数
if __name__ == '__main__':
    # m为全局变量
    for m in range(len(region_url)):
        first_line = "房屋简介,卧室,客厅,卫生间,面积(平方米),总价(万),小区,区,地址"
        # write_to_file(first_line)
        # 设置爬取的网页页数 全部是 (1, 61)，可以改少一点
        for i in range(1, 4):
            print("\n爬取 {} 第".format(region_name[m]) + str(i) + "页 信息\n")
            time.sleep(1)
            main(i)
            time.sleep(1)  # 每次循环延迟3秒，防止被封IP

