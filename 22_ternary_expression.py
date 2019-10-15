"""
    表达式1 if 条件 else 表达式2 构成一个表达式。
    
    整个表达式的值，是这样计算的，如果if 后面的条件为真，
    整个三元操作符构成的表达式值为表达式1的值，
    如果为假，整个表达式的值为表达式2的值。 
"""

x, y = 1, 5
z = x if x > y else y   #  如果x > y, z = x 否则 z  = y
print(z) # 5
####
x, y = 6, 8
z = (lambda : x , lambda : y) [x > y]()
print([x > y])
print(z) # 6

z = (lambda : x , lambda : y)[x < y]()
print(z) # 8
###
z = (x, y)[x > y]
print(z)  # 6 

z = (x, y)[x < y]
print(z) # 8

###
z = {True: x, False: y}[x > y]
print(z) # 8

z = {True: x, False: y}[x < y]
print(z) # 6
###
z = (x > y) and x or y
print(z)  # 8

z = (x < y) and x or y
print(z)  # 6
