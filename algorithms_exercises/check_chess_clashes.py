"""
На шахматной доске N на N находятся M ладей (ладья бьет клетки на той же
горизонтали или вертикали до ближайшей занятой). Определите, сколько пар ладей
бьют друг друга. Ладьи задаются парами числе I и J, обозначающих координаты.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[tuple[int]] = [(2, 8), (4, 3), (7, 5), (7, 7), (7, 8)]  # 3
INPUT_2: list[tuple[int]] = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]  # 0

INPUT: list[tuple[int]] = INPUT_2


def axis_check(rock: tuple, axis: dict, coordinate_num: int):
    coordinate = rock[coordinate_num]
    if coordinate not in axis:
        axis[coordinate] = 0
    axis[coordinate] += 1
    return axis


def main():
    axis_x = {}
    axis_y = {}
    for rock in INPUT:
        axis_x = axis_check(rock=rock, axis=axis_x, coordinate_num=0)
        axis_y = axis_check(rock=rock, axis=axis_y, coordinate_num=1)
    # Для малого количества фигур допускается использовать генератор
    clashes = sum(
        (axis[key] - 1)
        for axis in (axis_x, axis_y)
        for key in axis if axis[key] > 1)
    # Для большого количества объектов циклы выгоднее генераторов
    # clashes = 0
    # for axis in (axis_x, axis_y):
    #     for key in axis:
    #         if axis[key] > 1:
    #             clashes += axis[key] - 1
    print(clashes)


if __name__ == '__main__':
    main()
