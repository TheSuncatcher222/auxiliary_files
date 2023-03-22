"""
Предоставлено поле (кнопки) 4x4. В каждой ячейке указана либо точка, либо
цифра от 1 до 9. В каждый момент времени t (от 1 до 9) игрок должен
одновременно нажать на все кнопки, на которых указана цифра t. Если игрок
сумел нажать все необходимые кнопки - он получает 1 балл. Игрок может
одновременно нажать не более чем на k кнопок за раз.

Необходимо найти максимальное количество баллов, которое может может получить
игрок за игру для заданной конфигурации поля.

В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы кнопки строки - по 4 символа в каждой без
пробелов. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Например, для k = 3 и матрицы ниже ответ: 2
1 2 3 1
2 . . 2
2 . . 2
2 . . 2
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: list[int, str] = [  # 2
    3,
    '1231',
    '2..2',
    '2.2.',
    '22..']

INPUT: list[int, str] = INPUT_1

GAMERS: int = 2
FIELD_ROWS: int = 4
T = range(1, 9 + 1)


def init_input() -> tuple:
    """Get "k" and field configuration."""
    max_nums_at_time: int = INPUT[0] * GAMERS
    chars_count: dict[str, int] = {str(num): 0 for num in range(1, 10)}
    chars_count['.'] = 0
    for i in range(FIELD_ROWS):
        row: str = INPUT[i + 1]
        for char in row:
            chars_count[char] += 1
    return max_nums_at_time, chars_count


def count_points(max_nums_at_time: int, chars_count: dict[str, int]) -> str:
    """Count maximum points."""
    result: int = 0
    for second in T:
        if 0 < chars_count[str(second)] <= max_nums_at_time:
            result += 1
    return result


def main():
    max_nums_at_time, chars_count = init_input()
    print(count_points(
        max_nums_at_time=max_nums_at_time, chars_count=chars_count))


if __name__ == '__main__':
    main()
