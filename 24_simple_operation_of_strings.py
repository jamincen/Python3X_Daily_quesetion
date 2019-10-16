"""
    字符串的三种表达方式
        . single quotes  '
        . double quotes  "
        . three quotes   '''  # multi-line string
"""

## 拼接字符串的方式
a = 'hello'
b = 'world'
print(a + ' ' + b)
print(a, b)
print('%s %s' % (a, b))  # 推荐，效率高
print('hello''world')
print('{}{}'.format(a, b))  # 推荐，效率高
print(''.join(['hello', 'world']))

## 字符串常用的操作 
msg = 'python,java,javascript'
# 通过'，'分隔字符串，返回数组
print('\n 分隔字符串，: \n', msg.split(' '))
# 每次单词的首字母大写
print('\n 将字符串的所有单词首字母大写：\n', msg.title())
# 是否已python开头（startswith） 结尾(endswith)，如果是返回True，不是返回False
print('\n 是否已python开头: \n', msg.startswith('python'))
print('\n 是否已python结尾: \n', msg.endswith('python'))

print('\n 将字符串的第一个字符大写: \n', msg.capitalize())
print('\n 将所有字符大写: \n', msg.upper())
print('\n 将所有字符小写: \n', msg.lower())

## 字符串的截取、查找、替换
msg = 'abcdefgaaa'
print('\n 输出前3个字符: \n', msg[0: 3]) # 从0开始
print('\n 输出最后5个字符: \n', msg[-5:])
print('\n 替换字符a为v：\n', msg.replace('a', 'v'))
print('\n 查找元素c的位置: \n', msg.find('c'))# 从0开始，a-0，b-1,c-3
