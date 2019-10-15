### 深拷贝和浅拷贝

# id()查看变量内存地址
a = 'abc'
b = a
print(id(a), id(b))  # 5127616 5127616

# 变量.copy()  浅拷贝  只拷贝父对象，即第一层数据
a= ['a', 1, 'd', ['z', 'x', 'c']]
b = a.copy()

print(a)
print(b) #打印内容一样
# di() 内存地址不一样。证明浅拷贝会分配一个新的内存地址
print(id(a)) # 46008904
print(id(b)) # 46099464

# 修改a中的第一个元素
a[0] = 'A'
print(a) # ['A', 1, 'd', ['z', 'x', 'c']]
print(b) # ['a', 1, 'd', ['z', 'x', 'c']]  b并没有受到到影响

# 修改第四个元素中的第二个元素
a[3][1] = 'Q'
print(a) # ['A', 1, 'd', ['z', 'Q', 'c']]
print(b) # ['a', 1, 'd', ['z', 'Q', 'c']]  b也被修改了，但第一层数据没变

print(id(a[3]))  # 46820552
print(id(b[3]))  # 46820552


### 深拷贝 完全拷贝，无论多少层，数据都不会共享
#       需要 import copy
import copy
a = ['a', 1, 'd', ['z', 'x', 'c']]
b = copy.deepcopy(a)
print(id(a))
print(id(b)) # id 均不同

# 修改
a[0] = 'A'
a[3][0] = 'Q'
print(a) # ['A', 1, 'd', ['Q', 'x', 'c']]
# 深拷贝 任意层数据都是独立的，不会被修改
print(b) # ['a', 1, 'd', ['z', 'x', 'c']]


