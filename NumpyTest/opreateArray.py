# coding=utf-8

import numpy as np

# 切片
ten = np.arange(1, 11)
print(ten)

print(ten[2])  # 单个元素,从前往后
print(ten[-2])  # 从后往前

print(ten[2:5])  # 区间切片，默认步长为1
print(ten[1:7:2])  # 指定步长为2
print(ten[-1::-1])  # 步长为负时，从后往前

# 索引
print(ten[[0, 2, 3]])  # 使用数组作为索引，取多个元素

# 二维数组
ten.shape = (2, 5)
print('ten:', ten)

print(ten[1, 3])  # 二维数组取单个元素，第二行第四个
print(ten[0])  # 第一行所有元素
print(ten[0, :])  # 第一行所有元素
print(ten[1:, :])  # 除第一行外，剩下的所有
print(ten[:, ::2])  # 所有行，间隔一列选取数据
print(ten[:, [1, 4]])  # 所有行，用数组指定选择的列


# 变形与统计
arr1 = ten.reshape([1, 10])
print(arr1)
arr2 = ten.reshape([5, 2])
print('arr2:')
print(arr2)
print('ndim: {} shape: {} '.format(arr2.ndim, arr2.shape))

# 描述性统计方法
lst = np.array([[[1, 2, 3, 4],
                 [5, 6, 7, 8]],
                [[4, 2, 2, 5],
                 [3, 6, 8, 6]],
                [[1, 6, 8, 4],
                 [2, 3, 5, 7]]])
# sum
print('lst sum0:', lst.sum(axis=0))
print('lst sum1:', lst.sum(axis=1))
print('lst sum2:', lst.sum(axis=2))

# max min mul div square dot
print('min', lst.min())
print('min0', lst.min(axis=1))

# add sub
lst1 = np.array([1, 3, 5, 7], dtype=float)
lst2 = np.array([2, 4, 6, 8])

print('ADD:', lst1+lst2)
print('SUB:', lst2-lst1)
print('MUL:', lst2*lst1)
print('DIV:', lst2/lst1)
print('Square:', lst2**2)
print('dot', np.dot(lst1, lst2))
print('dot2', np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))

#  数组合成和分离
print('cancatenate:', np.concatenate((lst1, lst2), axis=0))
# 简便方法合成
print('hstack:', np.hstack(lst1))
print('vstack:', np.vstack(lst1))

