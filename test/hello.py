#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 模块第一个字符串为文档解释

' a test module'

# 公开后展示的作者名字
__author__ = 'zjh'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello world!'
    elif len(args) == 2:
        print 'hello %s' % args[1]
    else:
        print 'too many arguments!'

if __name__ == '__main__':
    test()
