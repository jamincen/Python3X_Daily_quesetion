### 读取文件
# 内置函数 open()
# read()  readline()  readlines()
"""
file = open(file_name,mode='r',encoding=)

file_name: 文件路径
mode: 打开方式:默认'r'
encoding: 指定打开的编码

常用打开方式
    r: 只读，文件必须存在
    r+ :读写，文件必须存在
    w : 写，文件若存在，则清空内容，从头写入。若不存在自动创建
    w+ : 读写，文件若存在，则清空内容，从头写入。若不存在自动创建
    a ：写，文件若存在，则后面追加内容。若不存在自动创建
    a+ ：读写，文件若存在，则后面追加内容。若不存在自动创建
"""
## read()
#  较low的写法
try:
    file = open(r'C:\Python34\gushi',mode='r',encoding='utf-8')
    print(file.read(6))  # 读取前6个字符，不填，打印全部内容
except (FileNotFoundError, IOError) as e:
    print('文件异常')
finally:
    file.close()

# 高级操作
with open(r'C:\Python34\gushi', 'r', encoding='utf-8') as file:
    print(file.read())

## readline()
with open(r'C:\Python34\gushi', 'r', encoding='utf-8') as file:
    while 1:
        line = file.readline()
        if not line:
            break
        # 每读取一行内容有换行符
        # print(line)
        # print(line.strip())
        print(line.replace('\n', ''))
    
