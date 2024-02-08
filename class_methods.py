# @staticmethod – используется для создания метода,
# который ничего не знает о классе или экземпляре,через который он был вызван.
# Он просто получает переданные аргументы, без неявного первого аргумента,
# и его определение неизменяемо через наследование.


class Person():

    @staticmethod
    def is_adult(age):
        if age > 18:
            print(True)
        else:
            print(False)


ron = Person()
ron.is_adult(23)


# @classmethod – это метод, который получает класс в качестве неявного
# первого аргумента, точно так же, как обычный метод экземпляра
# получает экземпляр. Это означает, что вы можете использовать класс
# и его свойства внутри этого метода, а не конкретного экземпляра.

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()


###

class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError('The score must be between 0 ~ 100!')

Yang = Student()

Yang.score=99
print(Yang.score)
# 99
# Yang.score = 999
# ValueError: The score must be between 0 ~ 100!