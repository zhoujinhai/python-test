# coding=utf-8

# 函数最小化、曲线拟合
import numpy as np
from scipy import optimize
import matplotlib.pylab as plt

def f(x):
    return x**2 + 10*np.sin(x)

x = np.arange(-10, 10, 0.2)

# # 显示图像
# plt.plot(x, f(x))
# plt.show()

# 梯度下降(BFGS)法寻找函数最小值
bfMin = optimize.fmin_bfgs(f, 0)  # 给定初始值为0(取决于初始点位置，有可能找到局部最小)
print('bfMin:', bfMin)
bfMin2 = optimize.fmin_bfgs(f, 3)
print('bfMin2:', bfMin2)

# 采用暴力算法找到全局最小（数据量一大速度慢）
grid = (-10, 10, 0.1)
bfMin_global_brute = optimize.brute(f, (grid,))
print('bfMin_global_brute:', bfMin_global_brute)

# 找某个区间上的最低点
bfMin_local = optimize.fminbound(f, 0, 10)
print('bfMin_local:', bfMin_local)

# 寻找函数的根
root = optimize.fsolve(f, 1)  # 猜想在1附近
print('root:', root)

root2 = optimize.fsolve(f, -2) # 在-2.5处也有一个
print('root2:', root2)

# 曲线拟合
xdata = np.linspace(-10, 10, num=20)
ydata = f(xdata) + np.random.randn(xdata.size)

def f2(x, a, b):
    return a*x**2 + b*np.sin(x)  # 知道函数形式，需确定参数

guess = [2, 2]  # 通过curve_fit 确定参数
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess)
print('params:', params)

# 图像显示拟合效果
def curve_f(x):
    return params[0]*x**2 + params[1]*np.sin(x)

plt.figure()
plt.plot(x, f(x), label='f(x)')
plt.plot(x, curve_f(x), 'r--', label='curve fit result')
plt.plot(root, f(root), 'g*', label='roots')
plt.plot(root2, f(root2), 'g*')
plt.plot(bfMin, f(bfMin), 'k.', 50, label='Minima')
plt.plot(bfMin2, f(bfMin2), 'k.', 50)
plt.legend(loc='upper center')
plt.show()

