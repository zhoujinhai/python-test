# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
# support CN's title
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=12)

# scatter 散点图
fig = plt.figure()
fig.add_subplot(3, 3, 1)
n = 30
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
t = np.arctan2(y, x)  # random-color

plt.scatter(x, y, c=t, s=25, marker='o', alpha=0.8)

plt.title(u'散点图', fontproperties=font)
plt.legend()

# bar 条形图
fig.add_subplot(332)
n = 5
x = np.arange(n)
y1 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)
y2 = (1-x/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(x, y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(x, y1):  # 添加注释
    plt.text(x+0.04, y+0.05, '%.2f' % y, ha='center', va='bottom')

plt.title(u'条形图', fontproperties=font)

# pie 饼图
fig.add_subplot(333)
n = 5
x = np.ones(n)
print(x)
cols = ['c', 'm', 'r', 'b', 'g']
x[-1] *= 2
plt.pie(x, explode=x*0.05, colors=cols, autopct='%1.1f%%')
plt.gca().set_aspect('equal')  # 保证饼图是圆形

# ploar 极坐标图
fig.add_subplot(334, polar=True)
n = 20
theta = np.arange(0.0, 2*np.pi, 2*np.pi/n)
radii = 10*np.random.rand(n)
# plt.plot(theta, radii)
plt.polar(theta, radii)

# heatmap 热图
fig.add_subplot(335)
from matplotlib import cm  # 上色用
data = np.random.rand(3, 3)
cmap = cm.Reds
print(data)
plt.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto')

# 3d图
from mpl_toolkits.mplot3d import axes3d

fig.add_subplot(336, projection='3d')

x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 2]
z = [1, 2, 6, 3, 2]

plt.plot(x, y, z)

# 热力图
fig.add_subplot(313)
def f(x, y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
x, y = np.meshgrid(x, y)
plt.contourf(x, y, f(x, y), 8, alpha=0.75, cmap=plt.cm.hot)
plt.title(u'热力图', fontproperties=font)

plt.savefig('./otherPic.png')
plt.show()













