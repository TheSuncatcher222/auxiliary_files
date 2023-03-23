"""
Узник замка проделал в стене прямоугольное отверстие DxE. Замок сделан из
прямоугольных кирпичей размеров AxBxC каждый.

Для заданных A, B, C, D, E напишите True, если кирпич пройдет в отверстие и
False - если нет. Все параметры представлены натуральными числами и указаны
через пробел.
"""

"""Примеры с ответами для тестов."""
INPUT_1 = '10 20 20 20 10'  # True
INPUT_2 = '10 20 20 10 10'  # False

INPUT = INPUT_1


def sort_two(first, second):
    """Sort ascending two numbers."""
    if first > second:
        return second, first
    return first, second


def main():
    a, b, c, d, e = list(map(int, INPUT.split()))
    a, b = sort_two(a, b)
    b, c = sort_two(b, c)
    a, b = sort_two(a, b)
    d, e = sort_two(d, e)
    if a <= d and b <= e:
        return print(True)
    return print(False)


if __name__ == '__main__':
    main()
