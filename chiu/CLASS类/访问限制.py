#       访问限制内部的变量不被外界访问
"""
只需要在定义属性的时候在属性前面加上
“__” 两个下划线即可

"""


class Info(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_info(self):
        print('%s:%s' % (self.__name, self.__age))


chiu = Info('chiudk', 18)
chiu.print_info()
#       print(chiu.__name)


'''
如果有访问限制，还想在外界获取类中的属性
或者是更改属性
可以在类中定义返回属性、修改属性的方法
'''


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score!')

    def print_info(self):
        print('%s得分(%s)' % (self.__name, self.__score))


chiudk = Student('邱登魁',96)
chiudk.print_info()

#       使用方法获取类中定义的属性
print(chiudk.get_name())
print(chiudk.get_score())

#       使用方法对类型的属性进行更改
chiudk.set_score(100)
print(chiudk.get_score())