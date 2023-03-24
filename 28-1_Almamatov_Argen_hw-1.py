class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname {self.fullname} '
              f'Age:{self.age}'
              f'IsMarried:{self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks.values())


class Teacher(Person):
    salary = 15000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def salaries(self):
        return self.salary + ((self.salary / 100 * 5) * (self.experience - 3)) if self.experience > 3 else self.salary


teacher = Teacher("Aleksey", 35, True, 8)
print(f'fullname: {teacher.fullname}\n'
      f'age: {teacher.age}\n'
      f'married: {teacher.is_married}\n'
      f'experience: {teacher.experience}\n'
      f'salary: {teacher.salaries()}\n')


def create_student():
    student1 = Student('Goga', 13, False, marks={
        'bio': 3,
        'math': 5,
        'english': 4
    })

    student2 = Student('Zeon', 15, False, marks={
        'bio': 3,
        'math': 5,
        'english': 2
    })2

    student3 = Student('Max', 32, True, marks={
        'bio': 5,
        'math': 5,
        'english': 5,
        'chemistry': 3
    })

    lst = [student1, student2, student3]
    return lst

lst1 = create_student()

for i in lst1:
    print(f'fullname: {i.fullname}\n'
          f'age: {i.age}\n'
          f'married: {i.is_married}\n'
          f'average_marks: {i.average()}\n')