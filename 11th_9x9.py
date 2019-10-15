### print()函数
#   seq: 分隔符，默认空格
#   end: 结束符，默认换行

for i in range(1,10):
    for j in range(1,i+1):
        # 输出 i * j, \t 代表tab键
        print("%d*%d=%d" % (j,i,i*j), end='\t')
    # 打印空字符，默认换行
    print('')
