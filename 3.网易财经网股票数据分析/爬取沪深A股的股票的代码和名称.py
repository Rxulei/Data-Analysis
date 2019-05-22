import re
from selenium import webdriver
import time
# 股票的数据放在一个表格table中，常规的requests + re 方法无法获取
# 故采用selenium进行获取，做到所见即所爬
# 确定K线 要四个数据 开盘价，收盘价，最高价，最低价
# 网易财经取爬取数据


def write_to_file(content):
    with open('沪深A股.csv', 'a', encoding='utf-8-sig') as f:
        f.write(str(content) + '\n')


# 解析HTML代码
def parse_page(html):
    pattern = re.compile('<tr.*?<td>.*?</td>.*?href.*?target.*?class.*?>(.*?)</a>.*?<td'
                         '.*?style.*?href.*?target.*?class.*?>(.*?)</a>.*?</td></tr>', re.S)  # re.S用来匹配换行符
    items = re.findall(pattern, html)

    for item in items:
        item = list(item)
        # print(item)
        s = ''
        for i in range(len(item)):
            s += item[i] + ','
        if len(s) < 13:
            print(s)
            # write_to_file(s)


def main():
    url = 'http://quotes.money.163.com/old/#query=EQA&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0'
    # url = 'http://quotes.money.163.com/old/#query=EQB&DataType=HS_RANK&sort=PERCENT&order=desc&count=24&page=0'
    browser = webdriver.Chrome()
    browser.get(url)
    print('\n获取第1页数据')
    time.sleep(2)
    html = browser.page_source
    parse_page(html)
    time.sleep(1)
    # 演示时候设置 爬取的页数范围 (2, 11)
    for m in range(2, 152):
        # 通过对应的文本内容找到了 下一页 按钮
        next_page = browser.find_element_by_partial_link_text('下一页')
        next_page.click()  # 不停地点击下一页按钮，进行翻页
        time.sleep(2)
        print('\n获取第' + str(m) + '页数据')
        time.sleep(1)
        html = browser.page_source
        parse_page(html)
        time.sleep(2)


# 启动主函数
if __name__ == '__main__':
    str_first = "股票代码,股票名称"
    # write_to_file(str_first)
    main()
