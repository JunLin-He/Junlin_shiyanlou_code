#!/usr/bin/env python3

from collections import Counter
import sys

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name
    def get_grade(self):
        pass


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        """
        以Pass: X, Fail: X 来统计自己的成绩情况
        （A,B,C 为 Pass, 如果得了 D 就认为是 Fail）
        """
        #student_count = Counter(pass=p, fail=f)
        #stu_list = {"pass": 0, "fail": 0}
        pass_count = 0
        fail_count = 0
        for g in self.grade:
            if g == 'D':
                fail_count += 1
            else:
                pass_count += 1
        print("Pass: {}, Fail: {}".format(str(pass_count), str(fail_count)))
            

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        """
        自动统计出老师班上学生的得分情况并按照频率的高低以
        A: X, B: X, C: X, D: X 的形式打印出来
        """
        stu_grade = Counter(self.grade)
        index = 1
        for k, v in stu_grade.items():
            if index == 4:
                print("{}: {}".format(k, str(v)))
            else:
                print("{}: {},".format(k, str(v)), end=' ')


def main():
    # 检查输入参数是否只有三个
    if len(sys.argv) != 3:
        print("Invalid input.")
        print("Usage:./student_teacher <<teacher> or <student>> <grade>")
        sys.exit(-1)

    # 检查输入的成绩是否只有A、B、C、D四个值
    grade_set = ['A', 'B', 'C', 'D']
    for grade in sys.argv[2]:
        if grade not in grade_set:
            print("Grade must be A or B or C or D!")
            sys.exit(-1)

    # 分情况讨论
    if sys.argv[1] == "teacher":
        teacher = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
        teacher.get_grade()
    elif sys.argv[1] == "student":
        student = Student('Kushal', 'CSE', 2005, sys.argv[2])
        student.get_grade()
    else:
        print("The second argument must be teacher or student.")
        sys.exit(-1)

if __name__ == '__main__':
    main()
'''
person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
'''