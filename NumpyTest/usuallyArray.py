# coding=utf-8

import numpy as np

# 两行四列的零数组
print(np.zeros([2, 4]))

# 元素全为1的数组
print(np.ones([2, 4]))

# 随机数(均匀分布)
print("Rand:")
print(np.random.rand(2, 4))
print(np.random.rand())  # 不带参数就是一个数
print("RandInt:")
print(np.random.randint(1, 20, 4))  # 范围加个数

# 正态分布
print("Randn:")
print(np.random.randn(2, 4))

# choice
print("Choice:")
print(np.random.choice([1, 3, 4, 5, 6]))

# 贝塔分布
print("BetaDistribute:")
print(np.random.beta(1, 10, 50))  # 取数范围和元素数量




