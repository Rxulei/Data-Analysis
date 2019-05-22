import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import MultiCursor  # 用于显示一条直线
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签,黑体simhei字体.
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号


# ----导入数据,绘制单个国家的失业率 折线图 和 散点图----------
# ------USA-------
unemployment_usa = pd.read_csv('美国历年失业率统计.csv', index_col=False)
unemployment_usa['时期'] = pd.to_datetime(unemployment_usa['时期'])
data_usa = unemployment_usa[::-1]  # 将数据逆置

print("\n----USA unemployment rate----")
print(data_usa)
print(data_usa['现值(%)'].describe())

mean_value_of_usa = data_usa['现值(%)'].mean()
std_of_usa = data_usa['现值(%)'].std()
min_value_of_usa = data_usa['现值(%)'].min()
max_value_of_usa = data_usa['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_usa['时期'], data_usa['现值(%)'], ls='-', lw=3, label='美国失业率变化趋势', c='red')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_usa['时期'], data_usa['现值(%)']):
    if count % 6 == 0:   # 每年的一月和七月 标出来对应的值
        plt.annotate(str(y), xy=(x, y + 0.3), xycoords='data', xytext=(x, y + 1.2), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.title('美国失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')

ax2 = fig.add_subplot(212)
plt.scatter(data_usa['时期'], data_usa['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_usa['时期'], data_usa['前值(%)'], color='blue', label='前月的值', s=7)
plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()


# -------CANADA-------
unemployment_canada = pd.read_csv('加拿大历年失业率统计.csv', index_col=False)
unemployment_canada['时期'] = pd.to_datetime(unemployment_canada['时期'])
data_canada = unemployment_canada[::-1]  # 将数据逆置
print("\n----CANADA unemployment rate----")
print(data_canada)
print(data_canada['现值(%)'].describe())

mean_value_of_canada = data_canada['现值(%)'].mean()
std_of_canada = data_canada['现值(%)'].std()
min_value_of_canada = data_canada['现值(%)'].min()
max_value_of_canada = data_canada['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_canada['时期'], data_canada['现值(%)'], ls='-', lw=3, label='加拿大失业率变化趋势', c='g')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_canada['时期'], data_canada['现值(%)']):
    if count % 6 == 0:
        plt.annotate(str(y), xy=(x, y + 0.1), xycoords='data', xytext=(x, y + 0.5), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()        # 把label中的数值放到一个框中
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.title('加拿大失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')
plt.xlabel('年份')

ax2 = fig.add_subplot(212)
plt.scatter(data_canada['时期'], data_canada['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_canada['时期'], data_canada['前值(%)'], color='blue', label='前月的值', s=7)
plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()

# -------JAPAN------
unemployment_japan = pd.read_csv('日本历年失业率统计.csv', index_col=False)
unemployment_japan['时期'] = pd.to_datetime(unemployment_japan['时期'])
data_japan = unemployment_japan[::-1]  # 将数据逆置
print("\n----JAPAN unemployment rate----")
print(data_japan)
print(data_japan['现值(%)'].describe())

mean_value_of_japan = data_japan['现值(%)'].mean()
std_of_japan = data_japan['现值(%)'].std()
min_value_of_japan = data_japan['现值(%)'].min()
max_value_of_japan = data_japan['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_japan['时期'], data_japan['现值(%)'], ls='-', lw=3, label='日本失业率变化趋势', c='b')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_japan['时期'], data_japan['现值(%)']):
    if count % 6 == 0:
        plt.annotate(str(y), xy=(x, y + 0.2), xycoords='data', xytext=(x, y + 0.7), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()
plt.grid(linestyle=":", color='black')
plt.title('日本失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')

ax2 = fig.add_subplot(212)
plt.scatter(data_japan['时期'], data_japan['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_japan['时期'], data_japan['前值(%)'], color='blue', label='前月的值', s=7)
plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()

# ------HongKong------
unemployment_hk = pd.read_csv('香港历年失业率统计.csv', index_col=False)
unemployment_hk['时期'] = pd.to_datetime(unemployment_hk['时期'])
data_hk = unemployment_hk[::-1]  # 将数据逆置
print("\n----HongKong unemployment rate----")
print(data_hk)
print(data_hk['现值(%)'].describe())

mean_value_of_hk = data_hk['现值(%)'].mean()
std_of_hk = data_hk['现值(%)'].std()
min_value_of_hk = data_hk['现值(%)'].min()
max_value_of_hk = data_hk['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_hk['时期'], data_hk['现值(%)'], ls='-', lw=3, label='香港失业率变化趋势', c='palegreen')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_hk['时期'], data_hk['现值(%)']):
    if count % 6 == 0:
        plt.annotate(str(y), xy=(x, y + 0.3), xycoords='data', xytext=(x, y + 0.6), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()
plt.grid(linestyle=":", color='black')
plt.title('香港失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')


ax2 = fig.add_subplot(212)
plt.scatter(data_hk['时期'], data_hk['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_hk['时期'], data_hk['前值(%)'], color='blue', label='前月的值', s=7)

plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()

# --------AUSTRALIA-------
unemployment_australia = pd.read_csv('澳大利亚历年失业率统计.csv', index_col=False)
unemployment_australia['时期'] = pd.to_datetime(unemployment_australia['时期'])
data_australia = unemployment_australia[::-1]  # 将数据逆置
print("\n----AUSTRALIA unemployment rate----")
print(data_australia)
print(data_australia['现值(%)'].describe())

mean_value_of_australia = data_australia['现值(%)'].mean()
std_of_australia = data_australia['现值(%)'].std()
min_value_of_australia = data_australia['现值(%)'].min()
max_value_of_australia = data_australia['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_australia['时期'], data_australia['现值(%)'], ls='-', lw=3, label='澳大利亚失业率变化趋势', c='chocolate')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_australia['时期'], data_australia['现值(%)']):
    if count % 6 == 0:
        plt.annotate(str(y), xy=(x, y - 0.1), xycoords='data', xytext=(x, y - 0.4), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()
plt.grid(linestyle=":", color='black')
plt.title('澳大利亚失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')

ax2 = fig.add_subplot(212)
plt.scatter(data_australia['时期'], data_australia['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_australia['时期'], data_australia['前值(%)'], color='blue', label='前月的值', s=7)
plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()

# ------ENGLAND------
unemployment_england = pd.read_csv('英国历年失业率统计.csv', index_col=False)
unemployment_england['时期'] = pd.to_datetime(unemployment_england['时期'])
data_england = unemployment_england[::-1]  # 将数据逆置
print("\n----ENGLAND unemployment rate----")
print(data_england)
print(data_england['现值(%)'].describe())

mean_value_of_england = data_england['现值(%)'].mean()
std_of_england = data_england['现值(%)'].std()
min_value_of_england = data_england['现值(%)'].min()
max_value_of_england = data_england['现值(%)'].max()

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(data_england['时期'], data_england['现值(%)'], ls='-', lw=3, label='英国失业率变化趋势', c='deeppink')

# 给折线图上的点标注数据
count = 0
for x, y in zip(data_england['时期'], data_england['现值(%)']):
    if count % 6 == 0:
        plt.annotate(str(y), xy=(x, y + 0.1), xycoords='data', xytext=(x, y + 0.4), textcoords="data",
                     color='blue', weight='bold', arrowprops=dict(arrowstyle="->", color='blue'))
    count += 1

plt.legend()
plt.grid(linestyle=":", color='black')
plt.title('英国失业率变化趋势', fontsize=16)
plt.ylabel('失业率(%)')

ax2 = fig.add_subplot(212)
plt.scatter(data_england['时期'], data_england['现值(%)'], color='red',  label='当月的值', s=7)
plt.scatter(data_england['时期'], data_england['前值(%)'], color='blue', label='前月的值', s=7)
plt.legend()
plt.grid(linestyle=":", color='green')  # 绘制刻度线的网格线
plt.ylabel('失业率(%)')
plt.xlabel('年份')

multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()


# -------------绘制合在一起的子图----------------------
# ------绘制一个2行3列的 折线子图 ------
fig = plt.figure()
fig.suptitle('各国失业率变化趋势对比', fontsize=16)

ax1 = fig.add_subplot(231)
plt.plot(data_usa['时期'], data_usa['现值(%)'], ls='-', lw=3, label='美国失业率变化趋势', c='r')
plt.legend()
plt.grid(linestyle=":", color='black')
plt.xticks(rotation=45)
plt.ylabel('失业率(%)')

ax2 = fig.add_subplot(232)
plt.plot(data_canada['时期'], data_canada['现值(%)'], ls='-', lw=3, label='加拿大失业率变化趋势', c='g')
plt.legend()
plt.grid(linestyle=":", color='black')
plt.xticks(rotation=45)
plt.ylabel('失业率(%)')

ax3 = fig.add_subplot(233)
plt.plot(data_japan['时期'], data_japan['现值(%)'], ls='-', lw=3, label='日本失业率变化趋势', c='b')
plt.legend()   # 把label中的数值放到一个框中
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.xticks(rotation=45)
plt.ylabel('失业率(%)')  # y的注释

ax4 = fig.add_subplot(234)
plt.plot(data_hk['时期'], data_hk['现值(%)'], ls='-', lw=3, label='香港失业率变化趋势', c='palegreen')
plt.legend()   # 把label中的数值放到一个框中
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.xticks(rotation=45)
plt.xlabel('年份')  # x轴的注释
plt.ylabel('失业率(%)')  # y的注释

ax5 = fig.add_subplot(235)
plt.plot(data_australia['时期'], data_australia['现值(%)'], ls='-', lw=3, label='澳大利亚失业率变化趋势', c='chocolate')
plt.legend()   # 把label中的数值放到一个框中
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.xticks(rotation=45)
plt.xlabel('年份')  # x轴的注释
plt.ylabel('失业率(%)')  # y的注释

ax6 = fig.add_subplot(236)
plt.plot(data_england['时期'], data_england['现值(%)'], ls='-', lw=3, label='英国失业率变化趋势', c='deeppink')
plt.legend()                   # 把label中的数值放到一个框中
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.xticks(rotation=45)
plt.xlabel('年份')  # x轴的注释
plt.ylabel('失业率(%)')  # y的注释

plt.show()


# ----在一张图中画出多个折线图----
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# USA
plt.plot(data_usa['时期'], data_usa['现值(%)'], ls='-', lw=3, label='美国失业率变化趋势', c='r')

# CANADA
plt.plot(data_canada['时期'], data_canada['现值(%)'], ls='-', lw=3, label='加拿大失业率变化趋势', c='g')

# JAPAN
plt.plot(data_japan['时期'], data_japan['现值(%)'], ls='-', lw=3, label='日本失业率变化趋势', c='b')

# HongKong
plt.plot(data_hk['时期'], data_hk['现值(%)'], ls='-', lw=3, label='香港失业率变化趋势', c='palegreen')

# AUSTRALIA
plt.plot(data_australia['时期'], data_australia['现值(%)'], ls='-', lw=3, label='澳大利亚失业率变化趋势', c='chocolate')

# ENGLAND
plt.plot(data_england['时期'], data_england['现值(%)'], ls='-', lw=3, label='英国失业率变化趋势', c='deeppink')

plt.legend(loc='upper right')
plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
plt.xlabel('年份')  # x轴的注释
plt.ylabel('失业率(%)')  # y的注释
plt.title('各国近十年失业率变化图', fontsize=16)  # 图片的标题

multi = MultiCursor(fig.canvas, (ax,), color='c', lw=2, horizOn=True, vertOn=True)
plt.show()

# 绘制各国失业率的 最大值，最小值，平均值，方差的柱状图
max_value = [max_value_of_usa, max_value_of_england, max_value_of_japan,
             max_value_of_australia, max_value_of_hk, max_value_of_canada]
min_value = [min_value_of_usa, min_value_of_england, min_value_of_japan,
             min_value_of_australia, min_value_of_hk, min_value_of_canada]
mean_value_of_unemployment_rate = [mean_value_of_usa, mean_value_of_england,
                                   mean_value_of_japan, mean_value_of_australia,
                                   mean_value_of_hk, mean_value_of_canada]
std = [std_of_usa, std_of_england, std_of_japan,
       std_of_australia, std_of_hk, std_of_canada]
tick_label = ['美国', '英国', '日本', '澳大利亚', '香港', '加拿大']
x = np.arange(len(tick_label))

bar_width = 0.2  # 柱状图的宽度
plt.bar(x, max_value, bar_width, color='r', label='失业率的最大值')
plt.bar(x+bar_width, min_value, bar_width, color='b', label='失业率的最小值')
plt.bar(x+2*bar_width, mean_value_of_unemployment_rate, bar_width, color='green', label='失业率的平均值')
plt.bar(x+3*bar_width, std, bar_width, color='yellow', label='失业率的标准差')

# 四种柱状图的数据标记
for a, b in zip(x, max_value):
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', size=10, weight='bold')
for a, b in zip(x, min_value):
    plt.text(a+bar_width, b, '%.2f' % b, ha='center', va='bottom', size=10, weight='bold')
for a, b in zip(x, mean_value_of_unemployment_rate):
    plt.text(a+2*bar_width, b, '%.2f' % b, ha='center', va='bottom', size=10, weight='bold')
for a, b in zip(x, std):
    plt.text(a+3*bar_width, b, '%.2f' % b, ha='center', va='bottom', size=10, weight='bold')

# 设置x轴的标签
plt.xticks(x+1.5*bar_width, tick_label)
plt.legend(loc='upper center')
plt.title('各国自2008年以来失业率数据统计图', fontsize=16)
plt.xlabel('国家')
plt.ylabel('失业率(%)')
plt.show()
