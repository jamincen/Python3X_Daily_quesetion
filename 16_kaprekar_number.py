"""
    什么是雷劈数？

印度数学家卡普列加（Dattaraya Ramchandra Kaprekar, 1905 - 1986）在一次旅行中，
遇到猛烈的暴风雨，他看到路边一块牌子被劈成了两半，一半上写着30，另一半写着25。
这时，他忽然发现30+25=55，55^2=3025，把劈成两半的数加起来，再平方，
正好是原来的数字。这种数字叫做雷劈数 或者 卡普利加数。(来自百度百科)

最小的雷劈数为81： 8+1=9 9² = 81

既然能一分为二说明这个数字的长度肯定是偶数，
知道这一点就很方便的能算出100万以内的雷劈数了。
"""

#for i in range(1000000):
#    i = str(i)
#    # filted string length is not even
#    if len(i) % 2 != 0:
#        continue
   
#    a = int(i[:int(len(i)/2)])
#    b = int(i[int(len(i)/2): ])

#    if (a + b) ** 2 == int(i):
#        print(i)
        
    
for j in range(1000000):
    
    a = len(str(j))
    if a % 2 != 0:
        continue
    else:
        b = 10 ** (a//2)
        
        x = int(j/b)
        y = int(j%b)
       # print(j,x,y)
        if (x + y)**2 == int(j):
            print(j)
