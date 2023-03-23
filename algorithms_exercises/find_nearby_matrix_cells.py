""""
Дана матрица. Для заданного элемента нужно вернуть список всех его
соседей в возрастающем порядке через пробел. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Например, для ячейки {0,0} соседями будут '0 2', для {2,1} - '1, 2, 7, 7'.
1 2 3
0 2 6
7 4 1
2 7 0

- В первой строке задано n — количество строк матрицы.
- Во второй — количество столбцов m. Числа m и n не превосходят 1000.
- В следующих n строках задана матрица. Элементы матрицы — целые числа, по
модулю не превосходящие 1000.
- В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.
"""

INPUT_1: list[str] = [  # 0 2
    '4',
    '3',
    '1 2 3',
    '0 2 6',
    '7 4 1',
    '2 7 0',
    '0',
    '0']
INPUT_2: list[str] = [  # 1 2 7 7
    '4',
    '3',
    '1 2 3',
    '0 2 6',
    '7 4 1',
    '2 7 0',
    '2',
    '1']
INPUT_3: list[str] = [  # 1 7
    '4',
    '1',
    '1',
    '0',
    '7',
    '2',
    '1',
    '0']
INPUT_5: list[str] = [  # 1 2
    '1',
    '3',
    '1 4 2',
    '0',
    '1']

INPUT: list[str] = INPUT_5


def read_input() -> tuple:
    """Read input data."""
    rows: int = int(INPUT[0])
    cols: int = int(INPUT[1])
    matrix: list = []
    for row in range(rows):
        matrix.append(list(map(int, INPUT[row + 2].split())))
    i: int = int(INPUT[-2])
    j: int = int(INPUT[-1])
    return rows, cols, matrix, i, j


def find_result(rows: int, cols: int, matrix: list, i: int, j: int) -> list:
    """Find nearby cells to cell {i, j}."""
    result: list = []
    if rows == 1:
        pass
    elif i == 0:
        result.append(matrix[i+1][j])
    elif i == rows - 1:
        result.append(matrix[i-1][j])
    else:
        result.append(matrix[i+1][j])
        result.append(matrix[i-1][j])
    if cols == 1:
        pass
    elif j == 0:
        result.append(matrix[i][j + 1])
    elif j == cols - 1:
        result.append(matrix[i][j - 1])
    else:
        result.append(matrix[i][j + 1])
        result.append(matrix[i][j - 1])
    result.sort()
    return result


def main():
    rows, cols, matrix, i, j = read_input()
    print(*find_result(rows=rows, cols=cols, matrix=matrix, i=i, j=j))


if __name__ == '__main__':
    main()
