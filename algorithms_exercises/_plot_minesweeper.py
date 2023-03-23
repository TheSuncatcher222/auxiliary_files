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
    '10 8 10',
    '1 2',
    '2 8',
    '3 4',
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
    for i in range(1, k):
        mines.append(list(map(int, INPUT[i].split())))
    return m, n, mines


def fill_field(field_framed: list[list[int]], mines: list[list[int]]):
    i, j = 0, 0
    add_one: list[int] = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
    for i, j in (mine for mine in mines):
        for i_add, j_add in (add for add in add_one):
            field_framed[i + i_add][j + j_add] += 1
    # for i, j in (mine for mine in mines):
    #     field_framed[i][j] = '*'
    return field_framed



def main():
    m, n, mines = read_input()
    # Создадим "рамку" вокруг поля, которая не будет учтена в ответе, для тех
    # индексов, который будут 'out of range'
    #field_framed = [[0] * (m + 2)] * (n + 2)
    #field_framed = fill_field(field_framed=field_framed, mines=mines)
    #field_framed[1][1] = 1
    field_framed = [[0]*2]*3
    field_framed[0][0] = 1
    print(field_framed)
    field_framed = [
        [0, 0],
        [0, 0],
        [0, 0]]
    field_framed[0][0] = 1
    print(field_framed)
    #for row in range(1,m):
    # for row in range(len(field_framed)):
    #     print(field_framed[row])



if __name__ == '__main__':
    main()
