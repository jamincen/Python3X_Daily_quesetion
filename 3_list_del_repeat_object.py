### 1.通过set方法
a = [1,2,3,1,1,1,7,9,5]
print(list(set(a))) # 自动排序

### 2.通过fromkeys创建新的字典
a = [1,2,3,1,1,1,7,9,5]
b = {}
b= b.fromkeys(a)
print(b)
c = list(b.keys())
print(c)

### 3.逻辑判断
a = [1,2,3,1,1,1,7,9,5]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)


