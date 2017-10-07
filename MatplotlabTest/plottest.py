# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

# 画出正弦和余弦函数图像
x = np.linspace(-np.pi, np.pi, 30, endpoint=True)
c, s = np.cos(x), np.sin(x)
plt.figure(1)

plt.plot(x, c, 'b-', marker='+', lw=2.5, label='cos')
plt.plot(x, s, 'g--', marker='*', lw=2.5, label='sin')

# 将坐标轴放中间
ax = plt.gca()
ax.spines['right'].set_color('none')  # 将右边和上边的边界设为不可见
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 把下边界和左边界移动到0点
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 规定x和y坐标点并将x上的3.14改为pi
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

# 给线条添加标签
plt.legend(loc='upper left')

# 标出特殊点
t = 2*np.pi/3
plt.plot([t, t], [0, np.cos(t)], color='red', linewidth=2, linestyle='--')
plt.scatter([t, ], [np.cos(t), ], 30, color='red')  # 画出需要注明的点
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# 坐标轴标记的刻度不被图像挡住
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.5))

# 添加网格
plt.grid()

plt.show()


