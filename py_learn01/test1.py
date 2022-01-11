class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count+1    #在类方法中直接修改类变量

# 测试:
if Student.count != 0:
    print('测试失败!1')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!2')
    else:
        lisa = Student('lisa')
        if Student.count != 2:
            print('测试失败!3')
        else:
            print('Students:', Student.count)    #这里输出的也是类变量
            print('测试通过!')