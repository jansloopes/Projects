from datetime import date
from datetime import time
from datetime import datetime


class Person:
    def ___init__(self, placeofbirth='', dateofbirth=date.today(), name=''):
        self.placeofbirth = placeofbirth
        self.dateofbirth = dateofbirth
        self.name = name

    def __repr__(self):
        return "({}".format(self.placeofbirth)


class Student(Person):
    def __init__(self, course, placeofbirth, dateofbirth, name, number=0):
        """

        :type course: object
        """
        super().__init__()
        self.number = number
        self.course = course
        self.placeofbirth = placeofbirth
        self.dateofbirth = dateofbirth
        self.name = name

    def __repr__(self):
        return "( {} {} {} {} {} )".format(self.course, self.number, self.placeofbirth, self.dateofbirth, self.name)

    def age(self):
        years = date.today().year - dateofbirth.year
        print ("{} {}".format (date.today().year, dateofbirth.year ))
        return years


class Course:
    def __init__(self, name='', number=0):
        self.name = name
        self.number = number

    def __repr__(self):
        return "({},{})".format(self.name, self.number)


dateofbirth = date(1956, 3, 13)
c1 = Course("programming", 1)
# s1 = Student( "programmin, dateofbirth, 1234)

# print(s1)
# print(s1.age())
# print(p1)

print(c1)
c2 = Student(c1, "amsterdam", dateofbirth, 'piet', 1235)
print(c2)
print(c2.age())
