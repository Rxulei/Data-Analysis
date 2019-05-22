import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
from matplotlib.widgets import MultiCursor
import matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
matplotlib.rcParams.update({'font.size': 12})  # 改变所有的字体大小

region_name = ['江宁区', '玄武区', '鼓楼区', '建邺区', '秦淮区',
               '雨花台区', '浦口区', '栖霞区', '六合区', '溧水区']
a_list = []  # 用来存放对应的 a
b_list = []  # 用来存放对应的 b


def model(a, b, x):
    return a*x + b  # y = ax + b


def cost_function(a, b, x, y):  # 代价函数
    m = len(x)
    return 1.0/2*m * (np.square(y-a*x-b)).sum()


def optimize(a, b, x, y):  # 优化函数  用的是梯度下降算法
    n = len(x)
    alpha = 0.2
    h_x = model(a, b, x)
    da = (1.0/n) * ((h_x - y)*x).sum()
    db = (1.0/n) * ((h_x - y).sum())
    a = a - alpha*da
    b = b - alpha*db
    return a, b


# 用一个2 * 2 的子图画出来 迭代次数还是10次试试
def iterate(a, b, x, y, times, i):
    count = 0
    time = 0
    previous_cost = 0
    x_max = x.max()
    x_min = x.min()
    x_mean = (x_max + x_min)/2.0
    y_max = y.max()
    y_min = y.min()
    y_mean = (y_max + y_min)/2.0
    for j in range(1, times):
        a, b = optimize(a, b, x, y)
        h_x = model(a, b, x)
        current_cost = cost_function(a, b, x, y)
        print('a=' + str('%.4f' % a), ' b=' + str('%.4f' % b), ' 误差为:' + str('%.2f' % current_cost))
        count = count + 1

        if count % 20 == 0:
            time = time + 1
            k = time % 4
            print('---------已经迭代{}次-----------------\n'.format(count))
            if k == 0:
                k = 4
            else:
                k = k
            plt.subplot(2, 2, k)
            plt.scatter(x, y, s=10)
            plt.plot(x, h_x, c='r')
            if k == 3 or k == 4:
                plt.xlabel('房子的面积(单位：百平方米)')  # x轴的注释
            plt.ylabel('价格(单位：百万)')  # y的注释
            plt.title('{}二手房 价格与面积关系图,循环第'.format(region_name[i]) + str(count) + '次')
            m = a * x_mean + b
            if b < 0:
                plt.annotate("y = "+str('%.4f' % a)+' * x '+str('%.4f' % b), xy=(x_mean, m), xytext=(x_mean * 0.4, y_mean *1.3),
                             weight='bold', color='c', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='c'))
            else:
                plt.annotate("y = " + str('%.4f' % a) + ' * x + ' + str('%.4f' % b), xy=(x_mean, m),
                             xytext=(x_mean * 0.4, y_mean * 1.3),
                             weight='bold', color='c',
                             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='c'))
            # plt.text(2, 20, "y = "+str('%.4f' % a)+' * x'+str('%.4f' % b), weight='bold', color='red')
            if k == 4:
                plt.show()

        # 当迭代一次，误差的变换值的绝对值小于10，就停止迭代
        if abs(current_cost - previous_cost) < 10:
            print('\n---------已经迭代{}次-----------------'.format(count))
            print('当前误差为: ' + str('%.2f' % current_cost) + ', 前一次的误差为: ' + str('%.2f' % previous_cost))
            value = current_cost - previous_cost
            value = float('%.2f' % value)
            print('两者的差值为 ' + str(abs(value)) + ' ,小于10, 所以停止循环')
            print('此时 a=' + str('%.4f' % a), ' b=' + str('%.4f' % b))
            b = b * 100
            print('将价格单位转换成:万，面积单位转换成:平方米 后')
            if b < 0:
                print('{}二手房 价格y(单位:万)与面积x(单位:平方米)预测模型为:\n'.format(region_name[i]) + 'y = '
                                                        '' + str('%.4f' % a) + ' * x ' + str('%.2f' % b) + '\n')
            else:
                print('{}二手房 价格y(单位:万)与面积x(单位:平方米)预测模型为:\n'.format(region_name[i]) + 'y = '
                                                            '' + str('%.4f' % a) + ' * x + ' + str('%.2f' % b) + '\n')
            a_list.append(a)  # 留着以后用
            b_list.append(b)  #
            plt.scatter(x, y, s=10)
            plt.plot(x, h_x, c='r')
            plt.xlabel('房子的面积(单位：百平方米)')  # x轴的注释
            plt.ylabel('价格(单位：百万)')  # y的注释
            plt.title('{}二手房 价格与面积关系图,循环第'.format(region_name[i]) + str(j) + '次')

            m = a * x_mean + b
            plt.text(x_mean*1.3, m*1.3, "y = " + str('%.4f' % a) + ' * x ' + str('%.4f' % b), weight='bold', color='c')
            plt.show()
            break
        previous_cost = current_cost


def query():
    for j in range(100):
        print('-------输入 0 查看 江宁区 的房价预测模型-------')
        print('-------输入 1 查看 玄武区 的房价预测模型-------')
        print('-------输入 2 查看 鼓楼区 的房价预测模型-------')
        print('-------输入 3 查看 建邺区 的房价预测模型-------')
        print('-------输入 4 查看 秦淮区 的房价预测模型-------')
        print('-------输入 5 查看 雨花台区 的房价预测模型-------')
        print('-------输入 6 查看 浦口区 的房价预测模型-------')
        print('-------输入 7 查看 栖霞区 的房价预测模型-------')
        print('-------输入 8 查看 六合区 的房价预测模型-------')
        print('-------输入 9 查看 溧水区 的房价预测模型-------')
        print('-------输入 10 查看各个区的房价预测模型的折线图------')
        index = input('请输入你的选择:\n')
        if index == '10':
            print('------------------------------------------------------------------')
            print('    -------------南京各个区二手房房价预测模型--------------------    ')
            x = range(50, 550)
            y0 = a_list[0] * x + b_list[0]
            y1 = a_list[1] * x + b_list[1]
            y2 = a_list[2] * x + b_list[2]
            y3 = a_list[3] * x + b_list[3]
            y4 = a_list[4] * x + b_list[4]
            y5 = a_list[5] * x + b_list[5]
            y6 = a_list[6] * x + b_list[6]
            y7 = a_list[7] * x + b_list[7]
            y8 = a_list[8] * x + b_list[8]
            y9 = a_list[9] * x + b_list[9]
            for i in range(len(region_name)):
                a = a_list[i]
                b = b_list[i]
                if b_list[i] < 0:
                    print('{} 二手房房价y(万)与面积(平方米)的预测模型为:  '.format(region_name[i]) + 'y = '
                        '' + str('%.4f' % a) + ' * x ' + str('%.2f' % b))
                else:
                    print('{} 二手房房价y(万)与面积(平方米)的预测模型为:  '.format(region_name[i]) + 'y = '
                        '' + str('%.4f' % a) + ' * x + ' + str('%.2f' % b))

            fig = plt.figure()

            ax1 = fig.add_subplot(211)
            plt.plot(x, y0, ls='-', lw=3, label=region_name[0] + ' 房价与面积的预测模型', c='r')
            ax1.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax1.set_yticks([50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1100, 1300, 1500, 1700, 1900])

            # plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[0]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            m = 300
            n = a_list[0] * m + b_list[0] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[0], '%.2f' % b_list[0]), weight='bold', color='c')

            ax2 = fig.add_subplot(212)
            plt.plot(x, y1, ls='-', lw=3, label=region_name[1] + ' 房价与面积的预测模型', c='c')
            ax2.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax2.set_yticks([50, 200, 350, 500, 650, 800, 950, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 3000])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[1]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            multi = MultiCursor(fig.canvas, (ax1, ax2), color='c', lw=2, horizOn=True, vertOn=True)

            n = a_list[1] * m + b_list[1] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[1], '%.2f' % b_list[1]), weight='bold', color='c')
            plt.show()

            fig = plt.figure()

            ax3 = fig.add_subplot(211)
            plt.plot(x, y2, ls='-', lw=3, label=region_name[2] + ' 房价与面积的预测模型', c='blue')
            ax3.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax3.set_yticks([100, 250, 450, 600, 750, 900, 1050, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            # plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[2]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            n = a_list[2] * m + b_list[2] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[2], '%.2f' % b_list[2]), weight='bold', color='c')

            ax4 = fig.add_subplot(212)
            plt.plot(x, y3, ls='-', lw=3, label=region_name[3] + ' 房价与面积的预测模型', c='gold')
            ax4.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax4.set_yticks([50, 200, 350, 500, 650, 800, 950, 1100, 1250, 1500, 1800, 2100, 2400, 2700, 2900])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.legend(loc='upper left')  # 将图例放在左上角
            plt.title('南京{}二手房房价预测模型'.format(region_name[3]))
            multi = MultiCursor(fig.canvas, (ax3, ax4), color='c', lw=2, horizOn=True, vertOn=True)
            n = a_list[3] * m + b_list[3] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[3], '%.2f' % b_list[3]), weight='bold', color='c')
            plt.show()

            fig = plt.figure()

            ax5 = fig.add_subplot(211)
            plt.plot(x, y4, ls='-', lw=3, label=region_name[4] + ' 房价与面积的预测模型', c='darksalmon')
            ax5.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax5.set_yticks([50, 200, 350, 500, 650, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2500, 2750, 3000])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            # plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[4]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            n = a_list[4] * m + b_list[4] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[4], '%.2f' % b_list[4]), weight='bold', color='c')

            ax6 = fig.add_subplot(212)
            plt.plot(x, y5, ls='-', lw=3, label=region_name[5] + ' 房价与面积的预测模型', c='black')
            ax6.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax6.set_yticks([50, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.legend(loc='upper left')  # 将图例放在左上角
            plt.title('南京{}二手房房价预测模型'.format(region_name[5]))
            multi = MultiCursor(fig.canvas, (ax5, ax6), color='c', lw=2, horizOn=True, vertOn=True)
            n = a_list[5] * m + b_list[5] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[5], '%.2f' % b_list[5]), weight='bold', color='c')
            plt.show()

            fig = plt.figure()
            ax7 = fig.add_subplot(211)
            plt.plot(x, y6, ls='-', lw=3, label=region_name[6] + ' 房价与面积的预测模型', c='darkcyan')
            ax7.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax7.set_yticks([50, 150, 250, 350, 450, 600, 750, 900, 1050, 1200, 1350, 1500, 1700])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            # plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[6]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            n = a_list[6] * m + b_list[6] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[6], '%.2f' % b_list[6]), weight='bold', color='c')

            ax8 = fig.add_subplot(212)
            plt.plot(x, y7, ls='-', lw=3, label=region_name[7] + ' 房价与面积的预测模型', c='lightblue')
            ax8.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax8.set_yticks([50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1300, 1500, 1700, 1900])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.legend(loc='upper left')  # 将图例放在左上角
            plt.title('南京{}二手房房价预测模型'.format(region_name[7]))
            multi = MultiCursor(fig.canvas, (ax7, ax8), color='c', lw=2, horizOn=True, vertOn=True)
            n = a_list[7] * m + b_list[7] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[7], '%.2f' % b_list[7]), weight='bold', color='c')
            plt.show()

            fig = plt.figure()

            ax9 = fig.add_subplot(211)
            plt.plot(x, y8, ls='-', lw=3, label=region_name[8] + ' 房价与面积的预测模型', c='lime')
            ax9.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax9.set_yticks([50, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            # plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京{}二手房房价预测模型'.format(region_name[8]))
            plt.legend(loc='upper left')  # 将图例放在左上角
            n = a_list[8] * m + b_list[8] - 200
            plt.text(m, n, 'y = {} * x + {}'.format('%.2f' % a_list[8], '%.2f' % b_list[8]), weight='bold', color='c')

            ax10 = fig.add_subplot(212)
            plt.plot(x, y9, ls='-', lw=3, label=region_name[9] + ' 房价与面积的预测模型', c='orange')
            ax10.set_xticks(
                [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax10.set_yticks(
                [50, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000])
            # plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.legend(loc='upper left')  # 将图例放在左上角
            plt.title('南京{}二手房房价预测模型'.format(region_name[9]))
            multi = MultiCursor(fig.canvas, (ax9, ax10), color='c', lw=2, horizOn=True, vertOn=True)
            n = a_list[9] * m + b_list[9] - 200
            plt.text(m, n, 'y = {} * x {}'.format('%.2f' % a_list[9], '%.2f' % b_list[9]), weight='bold', color='c')
            plt.show()

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1)
            plt.plot(x, y0, ls='-', lw=3, label=region_name[0] + ' 房价与面积的预测模型', c='r')
            plt.plot(x, y1, ls='-', lw=3, label=region_name[1] + ' 房价与面积的预测模型', c='c')
            plt.plot(x, y2, ls='-', lw=3, label=region_name[2] + ' 房价与面积的预测模型', c='blue')
            plt.plot(x, y3, ls='-', lw=3, label=region_name[3] + ' 房价与面积的预测模型', c='gold')
            plt.plot(x, y4, ls='-', lw=3, label=region_name[4] + ' 房价与面积的预测模型', c='darksalmon')
            plt.plot(x, y5, ls='-', lw=3, label=region_name[5] + ' 房价与面积的预测模型', c='black')
            plt.plot(x, y6, ls='-', lw=3, label=region_name[6] + ' 房价与面积的预测模型', c='darkcyan')
            plt.plot(x, y7, ls='-', lw=3, label=region_name[7] + ' 房价与面积的预测模型', c='lightblue')
            plt.plot(x, y8, ls='-', lw=3, label=region_name[8] + ' 房价与面积的预测模型', c='lime')
            plt.plot(x, y9, ls='-', lw=3, label=region_name[9] + ' 房价与面积的预测模型', c='orange')
            multi = MultiCursor(fig.canvas, (ax,), color='c', lw=2, horizOn=True, vertOn=True)

            ax.set_xticks([50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550])
            ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2700, 3000])
            plt.grid(linestyle=":", color='black')  # 绘制刻度线的网格线
            plt.xlabel('房屋面积(平方米)')  # x轴的注释
            plt.ylabel('总价(万)')  # y的注释
            plt.title('南京各个区二手房房价预测模型')
            plt.legend(loc='upper left')  # 将图例放在左上角
            plt.show()

            print('\n输入 quit 退出程序, 输入其他返回主界面')
            judge = input()
            if judge == 'quit':
                sys.exit()
        else:
            index = int(index)
            if b_list[index] < 0:
                print('{}二手房 价格y(单位:万)与面积x(单位:平方米)预测模型为:\n'.format(region_name[index]) + 'y = ' + str(
                    '%.4f' % a_list[index]) + ' * x ' + str('%.2f' % b_list[index]) + '\n')
            else:
                print('{}二手房 价格y(单位:万)与面积x(单位:平方米)预测模型为:\n'.format(region_name[index]) + 'y = ' + str(
                    '%.4f' % a_list[index]) + ' * x + ' + str('%.2f' % b_list[index]) + '\n')
            for k in range(50):
                x = float(input("------请输入{}二手房的面积(单位：平方米)------\n".format(region_name[index])))
                print('------------------------------------------')
                y = a_list[index] * x + b_list[index]
                print("\n------预测的价格为(单位：万)--------------")
                print('%.2f' % y)
                print('------------------------------------------')
                print('\n输入 1 继续预测 ' + region_name[index] + ' 的房价, 输入 quit 退出程序,输入其他返回查询主界面')
                judge = input()
                if judge == '1':
                    pass
                elif judge == 'quit':
                    sys.exit()
                else:
                    break


def main():
    for i in range(len(region_name)):
        a = 0
        b = 0
        print('\n------读取 {}'.format(region_name[i]) + '二手房房价信息------')
        house_price = pd.read_csv('{}二手房房价信息.csv'.format(region_name[i]), index_col=False)
        area = house_price['面积(平方米)']
        price = house_price['总价(万)']
        x = list(area)
        y = list(price)
        # 下面把x，y转变成列向量(100 X 1)
        # 训练集(x,y)要进行归一化处理
        # 若没有进行归一化处理  会产生了溢出现象！
        x = np.reshape(x, newshape=(len(x), 1))/100
        y = np.reshape(y, newshape=(len(y), 1))/100
        times = 10000
        iterate(a, b, x, y, times, i)
    query()


if __name__ == '__main__':
    main()

