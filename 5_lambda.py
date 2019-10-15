### lambda

# 函数
def add(x, y):
    return x + y

# 不写命名
lambda_add = lambda x, y: x + y
print(lambda(1, 2))
print(add(1, 2))


# x的平方函数体
m = lambda x : x ** 2

print(m(1))
print(m(2))


# 无论任何数，都返回1
m = lambda x : 1

# 任意多个数求和
m = lambda *args : sum(args)
print(m(1, 2, 3)) # 6


m = lambda x : x if x < 10 else '-'
print(m(1)) # 1
print(m(5)) # 5
print(m(12)) # -


######  全局函数
### 1.sort函数 排序
sort(key=None,reverse=False)  # 默认升序排列

# print([[6, 1], [3, 2], [9, 4], [1, 5]]).sort(lambda x : x[0])
# 按照二维列表的第一个元素进行排列
# [(1, 5), (3, 2), (6, 1), (9, 4)]
print(sorted([(6, 1), (3, 2), (9, 4), (1, 5)], key=lambda x : x[0])

dict1 = {'c': 'v1', 'a': 'v2', 'b': 'v3'}
# 按照字典的键排序，如果按照值排序则lambda x : x[1],返回元组组成的列表
# [('a', 'v2'), ('b', 'v3'), ('c', 'v1')]
print(sorted(dict1.items(), key=lambda x : x[0]))

# 按照4-x的绝对值排序（离4距离的大小决定）
# [4, 3, 5, 2, 6, 1, 7]
print(sorted([4, 3, 5, 2, 6, 1, 7], key=lambda x : abs(4-x)))


### 2.filter函数 过滤
filter(function,Iterable)

# 过滤能被2整除的 --偶数
lst = filter(lambda x : x % 2 == 0,[1, 2, 3, 4, 5]) # [2, 4]
print(list(lst))

# 求 1- 100内的整数平方根
lst = filter(lambda x : math.sqrt(x) % 1 == 0,range(1, 101))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(lst))


### 3.map函数  映射
map(function,Iter)

# 对列表元素求平方
m = map(lambda x : x ** 2,[1, 2, 3, 4])
# [1, 4, 9, 16]
print(list(m))

# 两个列表，相同位置的元素相加
m = map(lambda x, y: x + y,[1, 2, 3, 5], [9, 8, 7, 5])
# [10, 10, 10, 10]
print(list(m))







