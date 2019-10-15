### 九宫格
# 1+ ... + 9 = 45 每行45/3 = 15
arr = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            # 3个不重复数相加等于15  集合
            if i + j + k == 15 and len({i, j, k}) == 3:
                arr.append([i, j, k])

# 遍历arr，得出符合条件的
for a1 in arr:
    for a2 in arr:
        for a3 in arr:
            # 不重复的9个元素  列表set()
            if len(set(a1 + a2 + a3)) == 9:
                sum1 = a1[0] + a2[0] + a3[0]
                sum2 = a1[1] + a2[1] + a3[1]
                sum3 = a1[2] + a2[2] + a3[2]
                sum4 = a1[0] + a2[1] + a3[2]
                sum5 = a1[2] + a2[1] + a3[0]
                if sum1 == sum2 == sum3 == sum4 == sum5:
                    print('-'*8)
                    print(a1)
                    print(a2)
                    print(a3)
                    print('-'*8)
