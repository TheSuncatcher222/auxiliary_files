"""
Для заданной конфигурации поля размеров NxM и количества мин K изобразите поле
с расставленными на нем минами, а также числовым указанием количества мин
вокруг для каждой клетки. Сами мины обозначьте символом *. Ячейки отделяйте
пробельным символом.

В первой строке ввода через пробел указаны размеры поля: N строк и M колон, а
также количество мин K. В последующих строках через пробел указаны координаты
каждой отдельной мины через пробел. Первая цифра обозначает номер строки, а
вторая - номер столбца поля. Например, координата {1, 1} указывает на левый
верхний угол поля.
"""

"""Примеры с ответами для тестов."""
# 1 * 1 0 0 0 1 1 1 0
# 1 1 2 1 1 0 1 * 1 0
# 1 1 3 * 3 1 2 2 2 1
# 1 * 4 * 3 * 1 1 * 1
# 1 2 * 2 2 1 1 1 2 2
# 0 1 1 1 0 0 1 1 2 *
# 0 0 0 0 0 0 1 * 2 1
# 0 0 0 0 0 0 1 1 1 0
INPUT_1: list[str] = [
    '8 10 10',
    '1 2',
    '2 8',
    '3 4',
    '4 2',
    '4 4',
    '4 6',
    '4 9',
    '5 3',
    '6 10',
    '7 8']

INPUT: list[str] = INPUT_1


def read_input() -> tuple[int, list[list[int]]]:
    """Read input data."""
    m, n, k = map(int, INPUT[0].split())
    mines: list[list[int]] = []
    for i in range(1, k + 1):
        mines.append(list(map(int, INPUT[i].split())))
    return m, n, mines


def fill_field(field_framed: list[list[int]], mines: list[list[int]]):
    """"""
    move_i: list[int] = [-1, -1, -1, 0, 0, 1, 1, 1]
    move_j: list[int] = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i, j in (mine for mine in mines):
        for add in range(8):
            field_framed[i + move_i[add]][j + move_j[add]] += 1
    for i, j in (mine for mine in mines):
        field_framed[i][j] = '*'
    return field_framed


def main():
    m, n, mines = read_input()
    # Create the field with a box around: for 'out of range' indexes for mines
    # near to the field's boarders
    field_framed = []
    for _ in range(m + 2):
        field_framed.append([0] * (n + 2))
    fill_field(field_framed=field_framed, mines=mines)
    for row in range(1, m + 1):
        print(*field_framed[row][1:11])


if __name__ == '__main__':
    main()
