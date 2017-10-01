# coding=utf-8

import numpy as np
from numpy.linalg import *
# 单位矩阵
print(np.eye(3))

lst = np.array([[1., 2.], [3., 4.]])

# 矩阵的逆
print('Inv:')
print(inv(lst))

# 矩阵的转秩
print('T:')
print(lst.transpose())

# 矩阵的行列式
print('Det:')
print(det(lst))

# 矩阵的特征值和特征向量
print('Eig:')
print(eig(lst))

# 解方程组
y = np.array(([5], [7]), dtype=float)
print('Slove:')
print(solve(lst, y))

# 协方差
print('Cov:')
print(np.cov(lst, lst, rowvar=False))

