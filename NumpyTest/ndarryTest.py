# coding=utf-8

import numpy as np

lst = [[1, 3, 5], [2, 4, 6]]
# print(type(lst))

arr = np.array(lst)
# print(type(arr))

# 定义ndarray类型(bool,int/8/16/32/64/128,uint8/16/32/64/128,float/16/32/64)
arr = np.array(lst, dtype=float)  # 默认float64

print(arr)

# 显示数组行列
print(arr.shape)
print("维度数:")
print(arr.ndim)
print('元素个数：')
print(arr.size)
print('数据类型：')
print(arr.dtype)
print('每个元素所占字节：')
print(arr.itemsize)



