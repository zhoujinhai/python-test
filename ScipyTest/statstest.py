# coding=utf-8

# 统计和随机数
import numpy as np
import matplotlib.pylab as plt
from scipy import stats

a = np.random.normal(size=1000)
bins = np.arange(-4, 5)
histogrm = np.histogram(a, bins=bins, normed=True)[0]
bins = 0.5*(bins[1:] + bins[:-1])
b = stats.norm.pdf(bins)  # norm是一种分布
plt.plot(bins, histogrm, 'r--')
plt.plot(bins, b, 'b-')
plt.show()

# 中位数
print('median:', np.median(a))
print('median:', stats.scoreatpercentile(a, 50))  # 50%
