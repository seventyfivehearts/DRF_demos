"""
写个匹配成绩的⼩程序，成绩有ABCDE 5个等级，与分数的对应关系如下
要求⽤户输⼊0-100的数字后，你能正确打印他的对应成绩等级，⽐如输⼊的是75，则打印C
A 90-100
B 80-89
C 60-79
D 40-59
E 0-39
"""
score = int(input('输入成绩：'))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 60 <= score <= 79:
    print('C')
elif 40 <= score <= 59:
    print('D')
else:
    print('E')
