"""
Есть матрица размера n × m (строки и столбцы соответственно). Нужно написать
функцию, которая её транспонирует.

В первой строке указывается количество строк n матрицы.
Во второй строке указывается количество столбцов m матрицы.
В следующих строках через пробел указываются числа матрицы построчно.
"""

INPUT_1: list[str] = [  # 1 0 7 2
    '4',                # 2 2 4 7
    '3',                # 3 6 1 0
    '1 2 3',
    '0 2 5',
    '7 4 1',
    '2 7 0']
INPUT_2: list[str] = [  # -7 5 3 9 2 -7 -3 1 -1
    '9',                # -1 -1 1 0 4 10 10 6 9
    '5',                # 0 2 -8 8 5 0 -7 -7 9
    '-7 -1 0 -4 -9',    # -4 2 -1 -8 2 -4 10 -5 1
    '5 -1 2 2 9',       # -9 9 -7 -1 8 -8 3 9 9
    '3 1 -8 -1 -7',
    '9 0 8 -8 -1',
    '2 4 5 2 8',
    '-7 10 0 -4 -8',
    '-3 10 -7 10 3',
    '1 6 -7 -5 9',
    '-1 9 9 1 9']
INPUT_3: list[str] = [  # 1 4 3 2
    '4',
    '1',
    '1',
    '4',
    '3',
    '2']
INPUT_4: list[str] = [  # 1
    '1',                # 3
    '3',                # 2
    '1 3 2']

INPUT: list[str] = INPUT_1


def main():
    n: int = int(INPUT[0])
    m: int = int(INPUT[1])
    transpose_matrix: list[list[int]] = []
    for row in range(m):
        transpose_matrix.append([])
    for origin_row in range(n):
        cells: list[int] = INPUT[2 + origin_row].split()
        for origin_column in range(m):
            transpose_matrix[origin_column].append(cells[origin_column])
    for row in range(m):
        print(*transpose_matrix[row])


if __name__ == '__main__':
    main()
