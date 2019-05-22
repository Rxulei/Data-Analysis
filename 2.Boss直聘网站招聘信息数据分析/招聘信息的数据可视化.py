import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文字体

# ---------导入4个CSV文件数据----------
# python
data_python = pd.read_csv('python.csv', index_col=False)

# Java
data_Java = pd.read_csv('Java.csv', index_col=False)

# C++
data_CPP = pd.read_csv('C++.csv', index_col=False)

# C
data_C = pd.read_csv('C.csv', index_col=False)


print('--------各岗位学历要求-------------------')
# ------绘制学历要求的柱状图--------
# python
fig2 = plt.figure()

ax1 = fig2.add_subplot(221)

print('\n')
print("python的学历要求")
print(data_python['学历要求'].value_counts())
plt.subplot(221)
data_python['学历要求'].value_counts().plot(kind='bar', rot=0, color='g', label="python学历要求")
plt.xlabel('学历要求')  # x轴的注释
plt.ylabel('公司个数')  # y的的注释
plt.legend()

b = data_python['学历要求'].value_counts().values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    # plt.text(a-0.15, b+5, '%.f' % b, size=10, weight='bold')
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')


# Java
print('\n')
print("Java的学历要求")
print(data_Java['学历要求'].value_counts())
ax2 = fig2.add_subplot(222)
data_Java['学历要求'].value_counts().plot(kind='bar', rot=0, color='y', label="Java学历要求")
plt.xlabel('学历要求')  # x轴的注释
plt.ylabel('公司个数')  # y的注释
plt.legend()

b = data_Java['学历要求'].value_counts().values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')

# CPP
print('\n')
print("C++的学历要求")
print(data_CPP['学历要求'].value_counts())
ax3 = fig2.add_subplot(223)
data_CPP['学历要求'].value_counts().plot(kind='bar', rot=0, color='b', label="C++学历要求")
plt.xlabel('学历要求')  # x轴的注释
plt.ylabel('公司个数')  # y的注释
plt.legend()

b = data_CPP['学历要求'].value_counts().values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
# C
print('\n')
print("C的学历要求")
print(data_C['学历要求'].value_counts())
ax4 = fig2.add_subplot(224)
data_C['学历要求'].value_counts().plot(kind='bar', rot=0, color='r', label="C学历要求")
plt.xlabel('学历要求')  # x轴的注释
plt.ylabel('公司个数')  # y的注释
plt.legend()

b = data_C['学历要求'].value_counts().values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
fig2.suptitle('各种岗位的不同学历要求的个数', fontsize=16)
plt.show()

# -----绘制 学历要求 的饼图-------
plt.subplot(221)
data_python['学历要求'].value_counts().plot(kind='pie', autopct='%1.2f%%')
plt.title('python各种学历要求的比例')
plt.legend()

plt.subplot(222)
data_Java['学历要求'].value_counts().plot(kind='pie', autopct='%1.2f%%')
plt.title('Jav各种学历要求的比例')
plt.legend()

plt.subplot(223)
data_CPP['学历要求'].value_counts().plot(kind='pie', autopct='%1.2f%%')
plt.title('C++各种学历要求的比例')
plt.legend()

plt.subplot(224)
data_C['学历要求'].value_counts().plot(kind='pie', autopct='%1.2f%%')
plt.title('C各种学历要求的比例')
plt.legend()

plt.show()

# ------------工作经验要求的 饼图--------
print('\n')
print('--------工作经验要求-----------------------------')
# python
print('\n')
print("python的工作经验要求")
print(data_python['工作经验'].value_counts())
plt.subplot(221)                                     # 文本标签的值精确到小数点后面两位
data_python['工作经验'].value_counts().plot(kind='pie', autopct='%1.2f%%',)
plt.title("python工作经验要求")


# Java
print('\n')
print("Java的工作经验要求")
print(data_Java['工作经验'].value_counts())
plt.subplot(222)
data_Java['工作经验'].value_counts().plot(kind='pie', autopct='%1.2f%%',)
plt.title("Java工作经验要求")


# C++
print('\n')
print("C++的工作经验要求")
print(data_CPP['工作经验'].value_counts())
plt.subplot(223)
data_CPP['工作经验'].value_counts().plot(kind='pie', autopct='%1.2f%%',)
plt.title("C++工作经验要求")


# C
print('\n')
print("C的工作经验要求")
print(data_C['工作经验'].value_counts())
plt.subplot(224)
data_C['工作经验'].value_counts().plot(kind='pie', autopct='%1.2f%%',)
plt.title("C工作经验要求")

plt.show()

# -------招聘人数 前10的公司 的柱状图----------
print('\n')
print('--------招聘人数前10公司名称--------------------------------')

# python
print('\n')
print("----python招聘人数前10公司名称----")
print(data_python['公司名称'].value_counts().head(10))

fig3 = plt.figure()

ax1 = fig3.add_subplot(221)

data_python['公司名称'].value_counts().head(10).plot(kind='bar', color='red', label="python招聘人数前10公司名称")
plt.xticks(rotation=30)
plt.ylabel('岗位个数')  # y的注释
plt.legend()

b = data_python['公司名称'].value_counts().head(10).values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
    
# Java
print('\n')
print("----Java招聘人数前10公司名称----")
print(data_Java['公司名称'].value_counts().head(10))

ax2 = fig3.add_subplot(222)
data_Java['公司名称'].value_counts().head(10).plot(kind='bar', color='blue', label="Java招聘人数前10公司名称")
plt.xticks(rotation=30)
plt.ylabel('岗位个数')  # y的注释
plt.legend()

b = data_Java['公司名称'].value_counts().head(10).values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')

# C++
print('\n')
print("----C++招聘人数前10公司名称----")
print(data_CPP['公司名称'].value_counts().head(10))

ax3 = fig3.add_subplot(223)
data_CPP['公司名称'].value_counts().head(10).plot(kind='bar', color='yellow', label="C++招聘人数前10公司名称")
plt.xticks(rotation=30)
plt.ylabel('岗位个数')  # y的注释
plt.legend()

b = data_CPP['公司名称'].value_counts().head(10).values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
    
# C
print('\n')
print("----C招聘人数前10公司名称----")
print(data_C['公司名称'].value_counts().head(10))

ax4 = fig3.add_subplot(224)
data_C['公司名称'].value_counts().head(10).plot(kind='bar', color='green', label="C招聘人数前10公司名称")
plt.xticks(rotation=30)
plt.ylabel('岗位个数')  # y的注释
plt.legend()

b = data_C['公司名称'].value_counts().head(10).values
number_list = []
for value in b:
    number_list.append(value)
x = np.arange(len(number_list))
for a, b in zip(x, number_list):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
fig3.suptitle('全国范围内招聘各种岗位的个数前十的公司', fontsize=16)
plt.show()

# ----------工作地点分布的 饼图--------
print('\n')
print('--------工作地点-----------------------')
# python
print('\n')
print("----python工作地点分布前20----")
print(data_python['工作地点'].value_counts().head(20))
plt.subplot(221)                              # 求出不同的工作地点的个数
data_python['工作地点'].value_counts().head(20).plot(kind='pie', autopct='%1.2f%%', explode=np.linspace(0, 1, 20))
plt.title("python工作地点分布")


# Java
print('\n')
print("----Java工作地点分布前15----")
print(data_Java['工作地点'].value_counts().head(15))
plt.subplot(222)
data_Java['工作地点'].value_counts().head(15).plot(kind='pie', autopct='%1.2f%%', explode=np.linspace(0, 1, 15))
plt.title("Java工作地点分布")


# C++
print('\n')
print("----C++工作地点分布前20----")
print(data_CPP['工作地点'].value_counts().head(20))
plt.subplot(223)
data_CPP['工作地点'].value_counts().head(20).plot(kind='pie', autopct='%1.2f%%', explode=np.linspace(0, 1, 20),)
plt.title("C++工作地点分布")


# C
print('\n')
print("----C工作地点分布前20----")
print(data_C['工作地点'].value_counts().head(20))
plt.subplot(224)
data_C['工作地点'].value_counts().head(20).plot(kind='pie', autopct='%1.2f%%', explode=np.linspace(0, 1, 20))
plt.title("C工作地点分布")

plt.show()

# 根据工作地点来统计平均工资 和前面的结合
# python
city_of_python = data_python['工作地点'].value_counts().head(10).index
city_list_of_python = []
for value in city_of_python:
    city_list_of_python.append(value)

min_wages_of_python = []
max_wages_of_python = []
for city in city_list_of_python:
    min_wages_of_python.append(data_python.loc[data_python['工作地点'] == city]['最低工资'].mean())
    max_wages_of_python.append(data_python.loc[data_python['工作地点'] == city]['最高工资'].mean())

print('\n--------全国主要城市python的平均工资--------')
for i in range(len(city_list_of_python)):
    print(city_list_of_python[i] + ' 最低工资的平均值 : ' + str('%.f' % min_wages_of_python[i]) + ', 最高工资的平均值 : ' + str('%.f' % max_wages_of_python[i]))

bar_width = 0.4

x = np.arange(len(city_list_of_python))
plt.bar(x, max_wages_of_python, bar_width, color='c', label='python最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_python, bar_width, color='r', label='python最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('工资的平均值(元)')
plt.legend()
plt.title('全国主要城市python的平均工资', fontsize=16)
plt.xticks(x+bar_width/2, city_list_of_python)

x = np.arange(len(max_wages_of_python))
for a, b in zip(x, max_wages_of_python):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_python))
for a, b in zip(x, min_wages_of_python):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式
plt.show()

# Java
city_of_java = data_Java['工作地点'].value_counts().head(10).index
city_list_of_java = []
for value in city_of_java:
    city_list_of_java.append(value)

min_wages_of_java = []
max_wages_of_java = []
for city in city_list_of_java:
    min_wages_of_java.append(data_Java.loc[data_Java['工作地点'] == city]['最低工资'].mean())
    max_wages_of_java.append(data_Java.loc[data_Java['工作地点'] == city]['最高工资'].mean())

print('\n----全国主要城市Java的平均工资----')
for i in range(len(city_list_of_java)):
    print(city_list_of_java[i] + ' 最低工资的平均值 : ' + str('%.f' % min_wages_of_java[i]) + ', 最高工资的平均值 : ' + str('%.f' % max_wages_of_java[i]))

x = np.arange(len(city_list_of_java))
plt.bar(x, max_wages_of_java, bar_width, color='c', label='Java最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_java, bar_width, color='r', label='Java最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('工资的平均值(元)')
plt.legend()
plt.title('全国主要城市Java的平均工资', fontsize=16)
plt.xticks(x+bar_width/2, city_list_of_java)

x = np.arange(len(max_wages_of_java))
for a, b in zip(x, max_wages_of_java):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_java))
for a, b in zip(x, min_wages_of_java):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式
plt.show()


# C++
city_of_CPP = data_CPP['工作地点'].value_counts().head(10).index
city_list_of_CPP = []
for value in city_of_CPP:
    city_list_of_CPP.append(value)


min_wages_of_CPP = []
max_wages_of_CPP = []
for city in city_list_of_CPP:
    min_wages_of_CPP.append(data_CPP.loc[data_CPP['工作地点'] == city]['最低工资'].mean())
    max_wages_of_CPP.append(data_CPP.loc[data_CPP['工作地点'] == city]['最高工资'].mean())

print('\n----全国主要城市C++的平均工资----')
for i in range(len(city_list_of_CPP)):
    print(city_list_of_CPP[i] + ' 最低工资的平均值 : ' + str('%.f' % min_wages_of_CPP[i]) + ', 最高工资的平均值 : ' + str('%.f' % max_wages_of_CPP[i]))

x = np.arange(len(city_list_of_CPP))
plt.bar(x, max_wages_of_CPP, bar_width, color='c', label='C++最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_CPP, bar_width, color='r', label='C++最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('工资的平均值(元)')
plt.legend()
plt.title('全国主要城市C++的平均工资', fontsize=16)
plt.xticks(x+bar_width/2, city_list_of_CPP)

x = np.arange(len(max_wages_of_CPP))
for a, b in zip(x, max_wages_of_CPP):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_CPP))
for a, b in zip(x, min_wages_of_CPP):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式
plt.show()


# C
city_of_C = data_C['工作地点'].value_counts().head(10).index
city_list_of_C = []
for value in city_of_C:
    city_list_of_C.append(value)

min_wages_of_C = []
max_wages_of_C = []
for city in city_list_of_C:
    min_wages_of_C.append(data_C.loc[data_C['工作地点'] == city]['最低工资'].mean())
    max_wages_of_C.append(data_C.loc[data_C['工作地点'] == city]['最高工资'].mean())

print('\n----全国主要城市C的平均工资----')
for i in range(len(city_list_of_C)):
    print(city_list_of_C[i] + ' : ' + '最低工资的平均值：' + str('%.f' % min_wages_of_C[i]) + ' 最高工资的平均值：' + str('%.f' %max_wages_of_C[i]))

x = np.arange(len(city_list_of_C))
plt.bar(x, max_wages_of_C, bar_width, color='c', label='C最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_C, bar_width, color='r', label='C最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('工资的平均值(元)')
plt.legend()
plt.title('全国主要城市C的平均工资', fontsize=16)
plt.xticks(x+bar_width/2, city_list_of_C)

x = np.arange(len(max_wages_of_C))
for a, b in zip(x, max_wages_of_C):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_C))
for a, b in zip(x, min_wages_of_C):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式
plt.show()

# 将平均工资绘制成子图
# python
fig4 = plt.figure()


ax1 = fig4.add_subplot(221)
x = np.arange(len(city_list_of_python))
plt.bar(x, max_wages_of_python, bar_width, color='c', label='python最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_python, bar_width, color='r', label='python最低工资的平均值')

plt.ylabel('平均工资(元)')
plt.legend()
plt.title('全国主要城市python的平均工资')
plt.xticks(x+bar_width/2, city_list_of_python)

x = np.arange(len(max_wages_of_python))
for a, b in zip(x, max_wages_of_python):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_python))
for a, b in zip(x, min_wages_of_python):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')

# java
ax2 = fig4.add_subplot(222)
x = np.arange(len(city_list_of_java))
plt.bar(x, max_wages_of_java, bar_width, color='c', label='Java最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_java, bar_width, color='r', label='Java最低工资的平均值')

plt.ylabel('平均工资(元)')
plt.legend()
plt.title('全国主要城市Java的平均工资')
plt.xticks(x+bar_width/2, city_list_of_java)

x = np.arange(len(max_wages_of_java))
for a, b in zip(x, max_wages_of_java):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_java))
for a, b in zip(x, min_wages_of_java):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式

# C++
ax3 = fig4.add_subplot(223)
x = np.arange(len(city_list_of_CPP))
plt.bar(x, max_wages_of_CPP, bar_width, color='c', label='C++最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_CPP, bar_width, color='r', label='C++最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('平均工资(元)')
plt.legend()
plt.title('全国主要城市C++的平均工资')
plt.xticks(x+bar_width/2, city_list_of_CPP)

x = np.arange(len(max_wages_of_CPP))
for a, b in zip(x, max_wages_of_CPP):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_CPP))
for a, b in zip(x, min_wages_of_CPP):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式

# C
ax4 = fig4.add_subplot(224)
x = np.arange(len(city_list_of_C))
plt.bar(x, max_wages_of_C, bar_width, color='c', label='C最高工资的平均值')
plt.bar(x + bar_width, min_wages_of_C, bar_width, color='r', label='C最低工资的平均值')

plt.xlabel('城市')
plt.ylabel('平均工资(元)')
plt.legend()
plt.title('全国主要城市C的平均工资')
plt.xticks(x+bar_width/2, city_list_of_C)

x = np.arange(len(max_wages_of_C))
for a, b in zip(x, max_wages_of_C):
    plt.text(a, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')
x = np.arange(len(min_wages_of_C))
for a, b in zip(x, min_wages_of_C):
    plt.text(a+bar_width, b, '%.f' % b, ha='center', va='bottom', size=10, weight='bold')  # 固定格式

fig4.suptitle('全国各种岗位的平均工资对比', fontsize=16)
plt.show()


# print(data_python['最高工资'].str.contains('薪'))  # 输出的是布尔值，表示最高工资这一列的元素值中是否有“薪”这个字
# print(data_python)
