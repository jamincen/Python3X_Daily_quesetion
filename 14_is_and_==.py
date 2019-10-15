"""
    the difference between 'is' and '=='
    Is and == are used to determine if two variables are equal

    Is: Determines whether the references of two variables are equal,
        the values are the same, and the references are not necessarily the same.
    ==: Determine whether the values of the two variables are equal.
        If the references are the same, the values must be the same.

    is 内存地址相等
    == 值相同
"""

# 只有数值和字符串类型  a is b 才是 True
a = 1
b = 1
print(a is b)  # True
print(a == b)  # True

a = "123"
b = "123"
print(a is b)  # True
print(a == b)  # True

# list,tuple,dict,set   a is b  # False
a = [1, 2, 3]
a = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True

a = (1, 2, 3)
a = (1, 2, 3)
print(a is b)  # False
print(a == b)  # True

a = {1, 2, 3}
a = {1, 2, 3}
print(a is b)  # False
print(a == b)  # True

"""
然而事实真是这样吗？

1、
实际上在python中，对于 -5 ~ 256 之间的整数(包含-5 和 256)都会初始化在内存中，
所以当给变量赋值时，如果在这个区间中，他们都是指向同一个内存地址。
如果一旦超过这个范围，或者非整数，则会分配新的内存空间。则会返回False。

在PyCharm中，因为对解释器做了优化，所以测试的时候哪怕超过这个范围
a is b 也是返回True。所以我们在终端进行测试。

2、
Python解释器有一个intern(字符串驻留)的机制，意思是同一个字符串只在常量池中
保存一份，所以创建两个一样的字符串，他们都是指向了常量池中相同的地址。
所以上述例子，也没有什么特别要解释的。

但是要注意的是，当字符串中有空格时，则不会触发intern机制
(在Pycharm中优化了解释器，仍然会触发)

"""
