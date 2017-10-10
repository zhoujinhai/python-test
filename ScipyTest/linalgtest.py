# coding=utf-8

# scipy的线性代数操作

import numpy as np
from scipy import linalg as slg

# 计算行列式
arr = np.array([[1, 2], [3, 4]])
detRes = slg.det(arr)
print('detRes:', detRes)

# 计算逆矩阵
iArr = slg.inv(arr)
print('iArr:', iArr)

# 奇异值分解
arr = np.arange(9).reshape((3, 3))+np.diag([1, 0, 1])

u, sigma, v = slg.svd(arr)
print(u, sigma, v)
# sig3 = np.mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])  # 重构原始矩阵
# newArr = u*sig3*v
# print('arr:', arr)
# print('newArr', newArr)
sig3 = np.diag(sigma)  # 重构原始矩阵
newArr = u.dot(sig3).dot(v)
print('arr:', arr)
print('newArr', newArr)

# QR
q, r = slg.qr(arr)
print('q:', q)
print('r:', r)

# 求解
b = np.array([6, 14])
arr = np.array([[1, 2], [3, 4]])
print('Solve:', slg.solve(arr, b))

# 特征值和特征向量
# arr = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
print('eig:', slg.eig(arr))

