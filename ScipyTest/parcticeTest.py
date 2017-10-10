# coding=utf-8
import numpy as np
import matplotlib.pylab as plt
from scipy import optimize

# exercise1 拟合某地区一年的温度
x = np.arange(1, 13, 1)
ymin = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
ymax = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]

def min_f(x, a, b):
    return a*np.exp(b/x)

params1, params_covariance = optimize.curve_fit(min_f, x, ymin)
print('params1:', params1)

def min_fit_f(x):
    return params1[0]*np.exp(params1[1]/x)


plt.figure()
plt.plot(x, ymin, 'r*', label='min')
plt.plot(x, min_fit_f(x), 'r-', label='min fit')
plt.plot(x, ymax, 'g.', label='max')
plt.xlabel('month')
plt.ylabel('T/C')
plt.legend()
plt.show()