# coding=utf-8

# name = raw_input('please input your name:')
# print 'hello %s ,welcome to the world, \"Good Luck To You!\"' % name

# print 10.0 / 3


# 规定取绝对值的数据类型
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('The data must be int or float')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
# print my_abs(2.72818)

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# print calc([1, 2, 5, 3])

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
# a = [1, 2, 5, 6]
# print calc(*a)

# def person(name, age, **kw):
#     print 'name:%s ,age:%s ,other:%s' % (name, age, kw)
#
# person('zjh', 22, city='xiangtan')

# 阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
#
# print fact(10)
#
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, result):
#     if num == 1:
#         return result
#     return fact_iter(num-1, num*result)
#
# print fact(10)

# 迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print key, d[key]
# for key, value in d.iteritems():
#     print key, value

# 通过collections 模块的Iterable 类型判断一个对象是否可迭代
# from collections import Iterable
# a = isinstance('abcd', Iterable)
# print a

# 裴波那契数列(将print 改为 field 即为 生成器)
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b, n = b, a+b, n + 1
#
# fib(10)

# 素数
# import math
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# print filter(is_prime, range(1, 101))

# 引用hello.py
# import hello
#
# hello.test()