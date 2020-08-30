"""
__get__,__set__,__delete__


自省是通过一定的机制查询到对象的内部结构

dir(obj)

　　dir(obj)可以获取一个对象所有的属性与方法，返回为列表（仅有属性或方法名称）

　　dir()是Python提供的一个API函数，dir()函数会自动寻找一个对象的所有属性(包括从父类中继承的属性和方法)

__dict__

　　__dict__字典中存储的是对象或类的部分属性，键为属性名，值为属性值
　　实例对象的__dict__仅存储与该实例相关的实例属性　　

　　类的__dict__存储所有实例对象共享的变量和函数(类属性，方法等)，类的__dict__并不包含其父类的属性和方法

dir()和__dict__的区别

　　1.dir()是一个函数，返回的是list，仅有属性名和方法名；

　　2.__dict__是一个字典，键为属性名，值为属性值；

　　3.dir()用来寻找一个对象的所有属性和方法（包括从父类中继承的属性和方法），包括__dict__中的属性和方法，__dict__是dir()的子集；

　　注： 并不是所有对象都拥有__dict__属性。许多内建类型就没有__dict__属性，如list，此时就需要用dir()来列出对象的所有属性和方法
"""


class Age:
    def __set__(self, instance, value):
        print('*' * 30)
        print('self: ' + str(self))
        print('instance: ' + str(instance))
        print('value: ' + str(value))
        print('*' * 30)
        self.value = value

    def __get__(self, instance, owner):
        print('#' * 30)
        print('self: ' + str(self))
        print('instance: ' + str(instance))
        print('owner: ' + str(owner))
        print('#' * 30)
        return self.value


class Person:
    age = Age()

    def __getattribute__(self, item):
        if item == 'age':
            return super().__getattribute__(item)
        else:
            return super().__getattribute__(item)


me = Person()
me.age = 30
print(me.age)
