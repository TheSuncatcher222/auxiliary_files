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


# Метаклассы - это классы, которые определяют поведение других классов.
# Они используются для изменения способа, которым Python создает и обрабатывает классы.
# Метаклассы могут быть полезны в следующих случаях:
#     - при необходимости динамического изменения поведения класса, например,
#     - если вы хотите добавить или удалить атрибут или метод класса во время выполнения программы.
#     - при создании классов из данных, которые не заранее известны. 
#       Например, вы можете создавать классы на основе определенных условий во время выполнения программы.
#     - Для создания фреймворков и библиотек, которые нужно настраивать
#       под конкретные требования и при этом сохранить простоту интерфейса.
#       Они также могут использоваться для создания классов с определенными свойствами,
#       например, классов, которые автоматически регистрируются в библиотеке
#       или классов, которые автоматически сериализуются и десериализуются для совместимости с другими системами.


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        dct['my_attribute'] = 42
        return super(MyMeta, cls).__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

print(MyClass.my_attribute)
