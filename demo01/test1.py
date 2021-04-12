# int是一个类，具体实现是由C语言写起来的(源码中写了pass是使用C开发的)
from copy import copy, deepcopy

from django.views import View

# print('a')
# int dict 是type类的对象
# int dict 继承object
# type是自己的对象


# a = [1, 2, 3, [1, 2, 3]]
# a1 = a
#
# a2 = copy(a)    # 浅拷贝  是拿a的值赋值给另一给内存地址，然后通过内存地址把值传给a2
# # a3 = deepcopy(a)
#
# def func():
#     b = 10
#
#     def inner():
#         a = 100
#         print(a)
#         print(b)
#
#     return inner
#
#
# c = func()
# print(c)  # <function func.<locals>.inner at 0x7f55c047a2f0>
# 装饰器是闭包函数的典型应用

# 典型的装饰器
# def wrapper(func):
#     def inner(*args, **kwargs):
#         # 代码
#         res = func(*args, **kwargs)
#         # 代码
#         return res
#
#     return inner
#
#
# def a():
#     print('test')
#
#
# # 没有语法糖的情况下
# a = wrapper(a)
# a()
#
# # 有语法糖的情况下
# @wrapper
# def a():
#     print('test')

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root123',
                       charset='utf8', database='test', port=3306)
# 获取游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 查出数据是字典数据
# 操作 定义一个sql
# sql = 'select id, name from book'
# cursor.execute(sql)
# ret = cursor.fetchall()

# 插入
# sql = 'insert into book(id, name) values(%s, %s)'
# cursor.execute(sql, [2, 'sz'])
# conn.commit()
# print(ret)

# 删除
# sql = 'delete from book where name=%s'
# cursor.execute(sql,['sz'])
# conn.commit()
