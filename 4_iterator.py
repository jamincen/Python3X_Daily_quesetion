### 迭代器 iterator

# 迭代器和迭代对象
# 1> 可迭代对象包含迭代器
# 2> 如果一个对象拥有__iter__方法，则为可迭代对象；
#    如果一个对象拥有next方法，则为迭代器
# 3> 定义可迭代对象，必须实现__iter__方法
#    定义迭代器，必须实现__iter__和next方法

a = [1,3,5]
print(type(a)) # <class 'list'>
from collections import Iterable
# 创建一个a的迭代对象
a_iter = iter(a)
print(type(a_iter))  # <class 'list_iterator'>


print(a_iter.__next__()) # 1
print(a_iter.__next__()) # 3
print(a_iter.__next__()) # 5
#print(a_iter.__next__()) # 迭代到最后一个元素时，会抛出StopIteration异常



for i in a_iter:
    print(i)

# 遍历try except break
while 1:
    try:
        print(a_iter.__next__())
    except StopIteration:
        print('结束')
        break


### 通过Iterator判断是否是迭代对象

from collections import Iterable
print(isinstance([], Iterable)) # True 列表
print(isinstance({}, Iterable)) # True 字典
print(isinstance('hello', Iterable)) # True 字符串


