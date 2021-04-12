# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __setitem__(self, key, value):
#         setattr(self, key, value)  # 反射
#
#     def __getitem__(self, item):
#         # def getattr(object, name, default=None): 方法的参数
#         return getattr(self, item)
#
#
# p = Person('name')
# p.name = 'aaa'
# print(p.name)
# p['name'] = 'bbb'  # TypeError: 'Person' object does not support item assignment
# """
# 不能设置[]，因为有__setitem__方法拦截 需要重写item方法
# """
# print(p.name)  #
#
# print(p['name'])  # TypeError: 'Person' object is not subscriptable

# class MyDic(dict):
#     def __setattr__(self, key, value):
#         print('对象点赋值，触发')
#         self[key] = value
#
#     def __getattr__(self, item):
#         print('对象点取值，触发')
#         return self[item]
#
#
# mydic = MyDic(name='ss', age=18)
# print(mydic.name)


# class Person(object):
#     def __enter__(self):
#         print('使用with管理的时候会触发')
#         print('进入with预计块时执行此方法，此方法有返回值会作为as 生命的变量')
#         return 'aa'
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('退出with代码的时候会触发')
#         print('1', exc_type)
#         print('2', exc_val)
#         print('3', exc_tb)
#
#
# with Person() as p:  # 当执行这句话的时候会触发 enter
#     print(p)
#     aa
# 退出with代码的时候会触发
# 1 None
# 2 None
# 3 None
# 当缩进执行完了会执行exit方法
import pymysql


# class Mysql:
#     def __enter__(self):
#         print('使用with管理的时候会触发')
#         print('进入with预计块时执行此方法，此方法有返回值会作为as 生命的变量')
#         self.cont = pymysql.connect()
#         return cont
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cont.close()
#         print('退出with代码的时候会触发')
#         print('1', exc_type)
#         print('2', exc_val)
#         print('3', exc_tb)
#
#
# with Mysql() as cont:  # 当执行这句话的时候会触发 enter
#     # 查询操作语句
#     print(cont)

