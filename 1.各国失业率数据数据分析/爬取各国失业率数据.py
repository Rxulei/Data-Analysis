import requests
from requests.exceptions import RequestException
import random
import re
import time

# 用于向硬盘写数据时取不同的文件名
data1 = ['美国历年失业率统计', '英国历年失业率统计', '日本历年失业率统计', '澳大利亚历年失业率统计', '加拿大历年失业率统计', '香港历年失业率统计']

# 用于改变URL中部分内容，从而获取其他网页的数据
data2 = ['0', '4', '4', '14', '3', '3', '5', '2', '7', '1', '8', '2']  # 美国, 英国，日本，澳大利亚，加拿大，香港


# 用于爬取数据时提示当前的数据的来源
nation = ['美国', '英国', '日本', '澳大利亚', '加拿大', '香港']

# 定义三个全局变量
i = 0
m = 0
n = 0


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
        header = {"User-Agent": random.choice(user_agent)}
        # 利用程序代码，伪装成浏览器向网页的服务器发出请求
        response = requests.get(url, headers=header)

        if response.status_code == 200:  # 状态码 200 为正常
            return response.text  # 返回网页html代码
        return None
    except RequestException:
        return None


# 解析一页的HTML代码
def parse_one_page(html):
    pattern = re.compile('<tr class="activetr">.*?<td class=.*?style.*?>(.*?)</td>.*?<td class=.*?style'
                         '=.*?>(.*?)</td>.*?<td class=.*?style=.*?>(.*?)</td>.*?<td class=.*?style=.*?>'
                         '.*?</td>', re.S)  # re.S用来匹配换行符
    items = re.findall(pattern, html)
    for item in items:
        item = list(item)
        # print(item)
        s = ''
        for it in item:
            it = it.strip()
            # print(it)  it就是每一行4个元素中的一个元素
            s += it + ','
        s = s.replace('年', '-')
        s = s.replace('月', '')
        s = s.replace('%', '')

        if len(s) > 16:
            print(s)  # print(len(s))
            write_to_file(s)


def main(offset):
    global n  # 修改全局变量的值，需要声明全局变量
    global m
    url = 'http://data.eastmoney.com/cjsj/foreign_{}_{}_'.format(data2[n], data2[n + 1]) + str(offset) + '.html'
    # 美国 http://data.eastmoney.com/cjsj/foreign_0_4.html
    html = get_one_page(url)
    parse_one_page(html)
    if i == 7:
        m = m + 1
        n = n + 2


# 启动主函数
if __name__ == '__main__':
    for x in range(6):
        print('\n')
        print('----------------------------')
        print('获取 ' + nation[x] + ' 的历年失业率')
        print('----------------------------')
        time.sleep(1)
        first_line = '时期,前值(%),现值(%)'
        write_to_file(first_line)
        for i in range(1, 8):
            print("\n爬取第 " + str(i) + " 页的数据")
            time.sleep(1)   # 最后演示时要加上
            main(i)
            time.sleep(1)  # 每次循环延迟1秒，防止被封IP





