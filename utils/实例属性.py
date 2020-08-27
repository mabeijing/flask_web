"""
__getattribute__ 对应实例.操作，如a.b; object.__dict__
1、对实例生效，对类不生效
2、实例(.)操作被调用时，会调用__getattribute__, 类(.)操作不会


__getattr__
1、是实例访问实例属性最后一步判断，如果没有__getattr__处理，则会抛出AttributeException

应用场景
1、根据给定的dict给实例添加属性
2、延迟注册场景
3、作为实例注册工厂
"""


class Person:
    def __init__(self, name):
        self.name = name

    def my_print(self):
        return self.name * 2


attrs_dict = {'sex': "男", 'name': Person}


class A:
    def __init__(self):
        self.id = 888

    def __getattribute__(self, item):
        print('__getattribute__ is called: ' + str(item))
        return super().__getattribute__(item)

    def __getattr__(self, item):
        if item not in self.__dict__:
            print('__getattr__ is called: ' + str(item))
            self.__dict__.update({item: attrs_dict.get(item, None)})
        return self.__dict__[item]


if __name__ == '__main__':
    a = A()
    print(a.__dict__)
    print('-' * 30)
    print(a.sex)
    print('-' * 30)
    me = a.name('光头强')
    print(me.my_print())
    print('-'*30)
    print(a.id)
