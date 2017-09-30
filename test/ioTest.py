# coding=utf-8


# f = open('./test.txt')
# print f.readlines()
# f.close()

# 加上错误处理
# try:
#     f = open('./test.txt')
#     print f.read()
# finally:
#     if f:
#         f.close()

# 读取时限制大小

# # 采用with 更加简洁
# with open('./test.txt') as f:
#     print f.read()

# 写入文件

with open('./test.txt', 'w') as f:
    f.write('welcome to the world!')

