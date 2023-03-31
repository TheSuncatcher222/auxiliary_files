"""
Необходимо эффективно реализовать структуру данных Дек, максимальный размер
которого определяется заданным числом. Дек должен обладать следующими методами:
- push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».
- push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».
- pop_front() – вывести первый элемент дека и удалить его.
Если дек был пуст, то вывести «error».
-pop_back() – вывести последний элемент дека и удалить его.
Если дек был пуст, то вывести «error».

В первой строке указано количество команд n. Во второй строке указано число m -
максимальный размер дека. В последующих m строках перечислены команды.

Результаты выполнения каждой команды должны выводиться с новой строки.
Для успешных push_back() и push_front() ничего выводить не нужно.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[str] = [      # 861
    '4',                    # -819
    '4',
    'push_front 861',
    'push_front -819',
    'pop_back',
    'pop_back']
INPUT_2: list[str] = [      # error
    '7',                    # error
    '7',                    # 648
    'pop_front',            # 741
    'pop_front',            # error
    'push_front 741',
    'push_front 648',
    'pop_front',
    'pop_back',
    'pop_front']

INPUT: list[str] = INPUT_2

DEQUE_COMMANDS: dict[str, any] = {
        'push_back': lambda deque, x: deque.push(pointer='back', value=x[1]),
        'push_front': lambda deque, x: deque.push(pointer='front', value=x[1]),
        'pop_back': lambda deque, x: deque.pop(pointer='back'),
        'pop_front': lambda deque, x: deque.pop(pointer='front')}

ERR_FULL: str = 'error'
ERR_EMPTY: str = 'error'


class Deque():
    """Структура данных "дек" с кольцевым буфером без возможности перезаписи
    существующих значений."""

    def __init__(self, max_volume: int):
        """Инициализация элементов дека."""
        self.__deque: list = [None] * max_volume
        self.__max_volume: int = max_volume
        self.__length: int = 0
        self.__head: int = 0
        self.__tail: int = -1

    def pop(self, pointer):
        """Вывод крайнего элемента с начала / конца.
        При пустом деке будет выведено 'error'."""
        if self.__length == 0:
            return print(ERR_EMPTY)
        if pointer == 'front':
            pointer = self.__head
            self.__head = (self.__head + 1) % self.__max_volume
        else:
            pointer = self.__tail
            self.__tail = (self.__tail - 1) % self.__max_volume
        self.__length -= 1
        return print(self.__deque[pointer])

    def push(self, pointer, value):
        """Вставка элемента в начало / конец.
        При заполнении дека будет выведено 'error'."""
        if self.__length == self.__max_volume:
            return print(ERR_FULL)
        if pointer == 'front':
            self.__head = (self.__head - 1) % self.__max_volume
            pointer = self.__head
        else:
            self.__tail = (self.__tail + 1) % self.__max_volume
            pointer = self.__tail
        self.__deque[pointer] = value
        self.__length += 1
        return


def main():
    n: int = int(INPUT[0])
    m: int = int(INPUT[1])
    my_deque: Deque = Deque(max_volume=m)
    for i in range(2, n + 2):
        command = INPUT[i].split()
        DEQUE_COMMANDS[command[0]](my_deque, command)


if __name__ == '__main__':
    main()
