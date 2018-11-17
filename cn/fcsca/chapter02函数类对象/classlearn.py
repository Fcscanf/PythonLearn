from people import People
class Student(People):
    sum = 0

    # 构造函数
    def __init__(self, name, age, score=0):
        # 初始化对象参数-局部变量改变不了全局变量
        self.name = name
        self.age = age
        self.score = score
        print(self.name)
        print(self.__dict__)

    # 定义私有方法
    def __marking(self, score):
        if score < 0:
            return '不能评价负分'
        self.score = score
        print(self.name + ' student\'score is: ' + str(self.score))

    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        pass

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x, y):
        print(Student.sum)
        print('This is a static method')


class Printer():
    def pring_file(self):
        print('name :' + self.name)
        print('age :' + str(self.age))


student = Student('fc', 18)
# 私有方法调用不了
# print(student.__marking(-1))
print(student.name)
print(student.age)

# student.pring_file()
# print(student.__init__())
