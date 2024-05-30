
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print(self.name, self.score)



if __name__ == '__main__':
    student1 = Student("wo","100")
    student1.print_score()
    