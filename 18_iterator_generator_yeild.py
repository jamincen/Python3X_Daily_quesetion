# iterable
arr = [1, 2, 3, 4]  # list string files  dict set
for i in arr:
    print(i)

# generator  # change [] to ()
gener = (i ** 2 for i in range(10))
for i in gener:
    print(i)
    # gener 只是一个对象，不会占用太多内存空间

# yield  相当于返回一个生成器，程序不会结束
# seem to return
def m():
    print('m() starting')
    while True:
        result = yield 1
        print('result = ', result)

g = m()
print(next(g))
print('*' * 10)
print(next(g))
print('&' * 10)
print(next(g))

"""
m() starting
1
**********
result =  None
1
&&&&&&&&&&
result =  None
1
"""
