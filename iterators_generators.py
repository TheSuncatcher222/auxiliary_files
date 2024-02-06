"""
Итератор (Iterator) нужен для:
    - доступа к содержимому агрегированных объектов без раскрытия их внутреннего представления;
    - для предоставления единообразного интерфейса с целью обхода различных агрегированных структур;
    - [желательно] поддержки нескольких активных обходов одного и того же агрегированного объекта (желательно, но не обязательно).
Итератор в python — это любой объект, реализующий метод __next__ без аргументов, который должен вернуть следующий элемент или ошибку StopIteration.
Также он реализует метод __iter__ и поэтому сам является итерируемым объектом.

Итерируемый объект - это любой Python объект который реализует метод __iter__.
Также должна быть функция iter() - для получения итератора из объекта (вызывает его метод __iter__).
Если метод не реализован, то она проверяет наличие метода __getitem__ и на его основе создается итератор. __getitem__ должен принимать индекс с нуля.
Если не реализован ни один из этих методов, тогда будет вызвано исключение TypeError.
Функцией iter() пользуется, например, цикл for для получения итератора.

Генератор в Python — это языковая конструкция, которую можно реализовать двумя способами: 
    - как функция с ключевым словом yield;
    - как генераторное выражение.
В результате вызова функции или вычисления выражения, получаем объект-генератор типа types.GeneratorType.
В объекте-генераторе определены методы __next__ и __iter__, то есть реализован протокол итератора,
с этой точки зрения, в Python любой генератор является итератором.

Концептуально, итератор — это механизм поэлементного обхода данных,
а генератор позволяет отложено создавать результат при итерации.
Генератор может создавать результат на основе какого то алгоритма или брать элементы из источника данных(коллекция, файлы, сетевое подключения и пр) и изменять их.
"""


def my_generator(start: int, stop: int):
    while start < stop:
        yield start
        start += 1
    return

a = my_generator(0, 2)

option: int = 3

if option == 1:
    try:
        print(next(a))
        print(next(a))
        print(next(a))
        print(next(a))
    except StopIteration:
        pass
elif option == 2:
    for i in a:
        print(i)


###############################################


class MyIterator:

    def __init__(self, iterable):
        self.package = iterable

    def __iter__(self):
        return MyIteratorIterable(self.package)


class MyIteratorIterable:

    def __init__(self, iterable):
        self.iterable = iterable
        self._pointer = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._pointer < (len(self.iterable) - 1):
            self._pointer += 1
            return self.iterable[self._pointer]
        else:
            raise StopIteration


a = MyIterator([1, 2, 3])

option: int = 1

if option == 1:
    """
    Объект MyIterator должен быть итератором: иметь метод __next__.
    TypeError: 'MyIterator' object is not an iterator.
    Но MyIterator не должен сам обладать методом, в цикле for используется iter(MyIterator).
    """
    a = iter(a)
    try:
        print(next(a))
        print(next(a))
        print(next(a))
        print(next(a))
        print(next(a))
        print(next(a))
    except StopIteration:
        pass
elif option == 2:
    """
    Объект MyIterator должен быть итерируемым объектом: возвращать итератор в методе __iter__.
    TypeError: 'MyIterator' object is not iterable.
    """
    for i in a:
        print(i)
