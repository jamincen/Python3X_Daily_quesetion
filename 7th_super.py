### super()函数 继承，调用父类的方法

# 父类
class Person():
    def speak(self):
        print('i can speak')

    def sing(self):
        print('i can sing')

    def rap(self):
        print('i can rap')

    def basketball(self):
        print('i can basketball')


# 继承
class Student(Person):
    pass

class Student1(Person):
    def study(self):
        print('i like study')

if __name__ == '__main__':
    # 实例化一个Student对象
    s = Student()
    s.rap()
    s.basketball()

    s1 = Student1()
    s1.rap()
    s1.study()
    
# 调用 super().父类方法
class A:
    def get_name(self):
        return 'my name is xiaoming'

class B(A):
    def my_info(self):
        print('i am 18 years old')
        # 调用父类A中的get_name函数
        print(super().get_name())
        print('i like rap and basketball')

if __name__ == '__main__':
    b = B()
    
    """
    i am 18 years old
    my name is xiaoming
    i like rap and basketball
    """
    b.my_info()

## 多继承  
class A:
    num = 1
    def method(self):
        print('A ..method')

class B:
    num = 2
    def method(self):
        print('B ..method')
        
class C(A, B):
    num = 3
    pass

if __name__ == '__main__':
    c = C()
    #print(C.__mro__) # 优先查找顺序C> A> B 
    print(c.num) # 3
    c.method() # A ..method

