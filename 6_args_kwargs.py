### 可变参数形式
#   *args : 元组类型
#   **kwargs : 字典类型参数

# 两个参数
def fun(name, age):
    print(name)
    print(age)

if __name__ == '__main__':
    fun('tom', 19)
# fun('lily')
# TypeError: fun() missing 1 required positional argument: 'age'


# 多个参数是
##   *args
def fun_arr(name, *args):
    print(name)
    print(args)

if __name__ == '__main__':
    fun_arr('tom')
    fun_arr('tom', 20, 'man', '篮球')

## **kwargs
def fun_dict(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    # 或通过get方式取参数的值
    print("my name is %s i'am %s years old, my phone number is %s"
           % (kwargs.get('name'), kwargs.get('age'), kwargs.get('mobile')))

if __name__ == '__main__':
    fun_dict(name='tom', age=18, mobile='17766666666')


### 补充
    # 可变参数允许多个任意参数，也允许不传参数
    # 两个参数同时存在时，*args 要放在 **kwargs 之前，否则编译错误
    # 通常情况下，都是将可变参数写在最后面

