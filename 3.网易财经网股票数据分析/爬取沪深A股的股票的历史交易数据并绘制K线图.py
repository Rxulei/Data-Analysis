import requests
import re
from requests.exceptions import RequestException
import random
import time
import pandas as pd  # 读取文件
import sys  # 用于结束整个程序
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import mpl_finance as mpf

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文字体
# 收盘价高于开盘价时，则开盘价在下收盘价在上，二者之间的长方柱用红色或空心绘出，称之为阳线；其上影线的最高点为最高价，下影线的最低点为最低价。
# 收盘价低于开盘价时，则开盘价在上收盘价在下，二者之间的长方柱用绿色或实心绘出，称之为阴线，其上影线的最高点为最高价，下影线的最低点为最低价
# K线图（蜡烛图）和 成交量的柱状图放在一起，做出子图
# 画 日K线，把每日的K线图放在一张纸上
# Matplotlib.finance模块提供了绘制K线图的函数candlestick_ohlc()
# mpf.candlestick_ohlc(ax,quotes,width=0.7,colorup='r',colordown='green') # 上涨为红色K线，下跌为绿色，K线宽度为0.7
# stock = pd.read_table()
# stock = stock[::-1] #逆序排列
# 在一张图中显示4条折线，不清楚，故要想办法做K线图
# 同一个坐标y轴上左右画图
# 柱状图上标出数据
# 按照最新价，涨幅 ，最低价，最高价 画各种图

# 沪深A股的股票数据信息
# 考虑让用户输入股票的代码，输出数据及K线图
the_name_and_index_of_stock = pd.read_csv('沪深A股.csv', index_col=False)
stock_index = the_name_and_index_of_stock['股票代码']
stock_name = the_name_and_index_of_stock['股票名称']

# 将pandas的对象类型(CSV文件某一列的数据)的元素转换成列表类型 []
stock_index = list(stock_index)
stock_name = list(stock_name)

# 将列表stock_index中的int类型元素转换成字符串类型，并且将字符串长度不满6的元素前面补0
index_list = []
for n in range(len(stock_index)):
    stock_index[n] = str(stock_index[n])
    if len(stock_index[n]) == 6:
        index_list.append(stock_index[n])
    else:
        stock_index[n] = stock_index[n].rjust(6, '0')  # 设置字符串长度为6并且右对齐，空出来的用‘l’填充
        index_list.append(stock_index[n])

# 用来改变某个股票的url中的年份，从而获得当年的股票数据
year = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002,
        2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980]


# 将爬取到的股票数据写入本地硬盘，根据p来变换写入的CSV文件名，p是用户输入的股票代码或名称在列表中的下标
def write_to_file(content):
    global p
    with open('{}({}).csv'.format(stock_name[p], stock_index[p]), 'a', encoding='utf-8-sig') as f:
        f.write(str(content) + '\n')


# 获取一页的源码
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
    pattern = re.compile('<tr class=.*?<td>(.*?)</td><td class.*?>(.*?)</td><td class.*?>(.*?)</td><td.*?>(.*?)'
                         '</td><td class.*?>(.*?)</td>.*?class.*?</td>.*?class.*?>.*?<td>(.*?)</td>.*?</tr>', re.S)
    items = re.findall(pattern, html)  # items是一个列表，其中的元素为元组
    for i in range(1, len(items)):  # 不要第0个元素
        items[i] = list(items[i])
        # print(items[i])  items[i]是一个列表，其中的元素为字符串
        for j in range(len(items[i])):
            a = ''
            for item in items[i]:
                item = item.replace(',', '')
                a += item + ','
        print(a)
        write_to_file(a)


# 绘制K线图
def k_curve():
    global p
    stock_data = pd.read_csv(stock_name[p] + '(' + index + ').csv', index_col=False)
    data = stock_data[::-1]  # 将数据逆置，即将数据改成按照时间升序进行排列
    print(data)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    opens = data['开盘价']
    closes = data['收盘价']
    highs = data['最高价']
    lows = data['最低价']

    mpf.candlestick2_ochl(ax1, opens, closes, highs, lows, width=3, colorup='red', colordown='green', alpha=0.6)
    plt.title(stock_name[p] + '(' + index + ') 所有历史数据的K线图')
    plt.xticks(rotation=45)
    plt.ylabel('价格(元)')
    plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线

    x_ticks = int(len(opens) / 20)  #
    ax1.set_xticks(range(0, len(data['日期']), x_ticks))
    ax1.set_xticklabels(data['日期'][::x_ticks], fontdict={'fontsize': 10})  # 将日期这一列的数据每隔x_ticks取出来作为x轴下标

    ax2 = fig.add_subplot(212)
    trade_number_of_data = data['成交量']
    trade_number = []
    for value in trade_number_of_data:
        trade_number.append(value)
    x = np.arange(len(trade_number))
    plt.bar(x, trade_number, ls='-', lw=1, color='c', label=stock_name[p] + '(' + index + ') 所有历史数据的成交量的柱状图')
    plt.legend()
    plt.xticks(rotation=45)
    plt.ylabel('成交量')
    plt.grid(linestyle=":", color='black')
    ax2.set_xticks(range(0, len(trade_number), x_ticks))
    ax2.set_xticklabels(data['日期'][::x_ticks], fontdict={'fontsize': 10})  # 将日期这一列的数据每隔x_ticks取出来作为x轴下标

    plt.show()

    # 下面绘制 年k线图
    for m in range(length_of_year):
        # 依次获得2019,2018,2017的数据
        year_of_stock_data = data[data['日期'].str.contains('{}'.format(year[m]))]

        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        opens = year_of_stock_data['开盘价']
        closes = year_of_stock_data['收盘价']
        highs = year_of_stock_data['最高价']
        lows = year_of_stock_data['最低价']

        mpf.candlestick2_ochl(ax1, opens, closes, highs, lows, width=3, colorup='red', colordown='green', alpha=0.6)
        plt.title(stock_name[p] + '(' + index + ') {} 年的K线图'.format(year[m]))
        plt.xticks(rotation=45)
        plt.ylabel('价格(元)')
        plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线

        if len(opens) < 20:
            x_ticks = 1
        else:
            x_ticks = int(len(opens) / 20)
        ax1.set_xticks(range(0, len(year_of_stock_data['日期']), x_ticks))
        ax1.set_xticklabels(year_of_stock_data['日期'][::x_ticks], fontdict={'fontsize': 10})  # 将日期这一列的数据每隔x_ticks取出来作为x轴下标

        ax2 = fig.add_subplot(212)
        trade_number_of_data = year_of_stock_data['成交量']
        trade_number = []
        for value in trade_number_of_data:
            trade_number.append(value)
        x = np.arange(len(trade_number))
        plt.bar(x, trade_number, ls='-', lw=1, color='c', label=stock_name[p] + '(' + index + ') {} 年成交量的柱'
                                                                                              '状图'.format(year[m]))
        plt.legend()
        plt.xticks(rotation=45)
        plt.ylabel('成交量')
        plt.grid(linestyle=":", color='black')
        ax2.set_xticks(range(0, len(trade_number), x_ticks))
        ax2.set_xticklabels(year_of_stock_data['日期'][::x_ticks], fontdict={'fontsize': 10})  # 将日期这一列的数据每隔x_ticks取出来作为x轴下标

        plt.show()


def main(page):
    global index
    url = 'http://quotes.money.163.com/trade/lsjysj_{}.html?year={}&season='.format(index, year[j]) + str(page)
    html = get_one_page(url)
    parse_one_page(html)


def get_length_of_year():                # 改URL的代码
    global index
    index = stock_index[p]
    url = 'http://quotes.money.163.com/trade/lsjysj_{}.html?year=2019&season=2'.format(index)
    html = get_one_page(url)
    pattern = re.compile('<option value=.*?>(.*?)</option>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    # print(len(items))  # 输出列表的长度，减去4个季度，4个无用的值，共减去8得到年份的个数
    global length_of_year
    length_of_year = len(items) - 8
    return length_of_year


# 启动主函数
if __name__ == '__main__':
    # for b in range(len(stock_index)):
    choice = '1'
    index_and_name_list = []
    for it in stock_index:
        index_and_name_list.append(it)
    for it in stock_name:
        index_and_name_list.append(it)

    for i in range(50):
        if choice == '1':
            index = input('请输入你要查询的 沪深A股 的股票代码(6位数字) 或者是股票的名称!\n')
            for item in index_and_name_list:
                if index == item:
                    p = index_and_name_list.index(item)  # item 在列表index_and_name_list中的下标
                    # 如果p小于股票代码的长度，p就是输入的代码在股票列表中的下标
                    if p <= len(stock_index):
                        pass
                        break
                    # 如果 p大于股票代码的长度，p- len(stock_index)是输入的股票名称对应的代码在股票代码列表中的下标
                    else:
                        p = p - len(stock_index)
                        break
            else:
                print('没有该股票代码或股票名称, 请重新输入正确的股票代码或股票名称!\n')
                judge = input('输入1继续查询, 输入其他则退出查询!\n')
                if judge == '1':
                    continue
                else:
                    sys.exit()  # 终止整个程序

            first_line = '日期,开盘价,最高价,最低价,收盘价,成交量'
            write_to_file(first_line)
            length_of_year = get_length_of_year()
            print('\n获取的股票为 ' + stock_name[p] + '(' + index + '),' + ' 已经上市了' + str(length_of_year) + '年.')
            time.sleep(3)
            for j in range(length_of_year):
                if j == 0:
                    print('\n爬取' + str(year[j]) + '的股票信息')
                    time.sleep(1)
                    for k in range(2, 0, -1):
                        main(k)
                        time.sleep(1)

                else:
                    print('\n爬取' + str(year[j]) + '的股票信息')
                    time.sleep(1)
                    for k in range(4, 0, -1):
                        main(k)
                        time.sleep(1)
        else:
            break
        j = int(input('\n输入 1 绘制 {} 的K线图\n'.format(stock_name[p] + '(' + index + ')')))
        if j == 1:
            k_curve()
        choice = input('\n输入 1 继续查询, 输入其他则退出查询!\n')
