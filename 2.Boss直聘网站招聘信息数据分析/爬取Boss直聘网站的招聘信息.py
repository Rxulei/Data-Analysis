import requests
from requests.exceptions import RequestException
import random
import re
from bs4 import BeautifulSoup

import time

# 用于向硬盘写数据时取不同的文件名
data1 = ['python', 'Java', 'C++', 'C']

# 用于改变URL中部分内容，从而获取其他网页的数据
data2 = ['9', '1', '2', '5']  # python, Java, C++, C

# 定义两个全局变量
i = 0
m = 0


def write_to_file(content):
    name = data1[m]
    file_name = '{}.csv'.format(name)
    with open(file_name, 'a', encoding='utf-8-sig') as f:
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
        header = {"User-Agent": random.choice(user_agent)}
        response = requests.get(url, headers=header)

        if response.status_code == 200:  # 状态码 200 为正常
            return response.text  # 返回网页html代码
        return None
    except RequestException:
        return None


# 解析一页的HTML代码
def parse_one_page(html):
    # 先用Beautiful Soup 进行标签提取，再用正则表达式提取
    soup = BeautifulSoup(html, 'lxml')
    target_html = soup.find_all(name='li')
    target_html = str(target_html)

    pattern = re.compile('<li>.*?<div class.*?<div class.*?<h3 class.*?<a.*?<div class="job-title">(.*?)</div>.*?<span.*?>(.*?)-(.*?)K.*?<div.*?</div>.*?<p>(.*?) .*?<em.*?</em>(.*?)<em.*?</em>(.*?)</p>.*?<div class="info-company">.*?<div class.*?<h3.*?<a.*?target=.*?>(.*?)</a>.*?<p>.*?</p>.*?<div.*?</div>.*?<a.*?</a>.*?</li>', re.S)
    items = re.findall(pattern, target_html)
    for item in items:
        item = list(item)
        for k, it in enumerate(item):  # 除去列表中的字符元素中的逗号
            it = it.replace(',', '')
            it = it.replace('，', '')
            if k == 1 or k == 2:  # 在最低工资和最高工资 后面加上 000
                it = it + '000'
            item[k] = it
        s = ''
        for j in range(len(item)):
             s += item[j] + ','
        print(s)
        write_to_file(s)


def main(page):
    global m
    global i
    url = 'https://www.zhipin.com/c100010000-p10010{}/?page='.format(data2[m]) + str(page) + '&ka=page-' + str(page)
    html = get_one_page(url)
    parse_one_page(html)
    if i == 10:
        m = m + 1


# 启动主函数
if __name__ == '__main__':
    for x in range(4):
        first_line = "岗位名称,最低工资,最高工资,工作地点,工作经验,学历要求,公司名称"
        write_to_file(first_line)
        print('\n获取{}的招聘信息'.format(data1[m]))
        time.sleep(1)
        for i in range(1, 11):
            print("\n爬取第" + str(i) + "页信息")
            time.sleep(1)
            main(i)
            time.sleep(1)  # 每次循环延迟3秒，防止被封IP




