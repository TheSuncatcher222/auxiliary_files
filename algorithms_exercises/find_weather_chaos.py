"""
Хаотичность погоды за n дней понимается количество дней, в которые
температура строго больше чем в день до (если существует) и в день после (если
существует).

Необходимо вывести единственным числом хаотичность погоды за данный период.
В первой строке ввода указывается количество дней, во второй - температуры.
Единственный день в периоде также является хаотичным.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[str] = [  # 3
    '7',
    '-1 -10 -8 0 2 0 5']
INPUT_2: list[str] = [  # 2
    '5',
    '1 2 5 4 8']
INPUT_3: list[str] = [  # 1
    '1',
    '0']
INPUT_4: list[str] = [  # 0
    '5',
    '1 1 1 1 1']
INPUT_5: list[str] = [  # 0
    '5',
    '1 1 0 1 1']

INPUT: list[str] = INPUT_1


def read_input() -> tuple[int, list[int]]:
    """Read input data."""
    cnt_days: int = int(INPUT[0])
    temps: list[int] = list(map(int, INPUT[1].split()))
    return cnt_days, temps


def count_chaos(cnt_days: int, temps: list[int]):
    """Count temperature chaos in given period."""
    if cnt_days == 1:
        return 1
    elif cnt_days == 2:
        if temps[0] != temps[1]:
            return 1
        return 0
    result: int = 0
    if temps[0] > temps[1]:
        result += 1
    for day_index in range(1, cnt_days - 1):
        if (temps[day_index] > temps[day_index - 1]
                and temps[day_index] > temps[day_index + 1]):
            result += 1
    if temps[cnt_days - 1] > temps[cnt_days - 2]:
        result += 1
    return result


def main():
    cnt_days, temps = read_input()
    print(count_chaos(cnt_days, temps))


if __name__ == '__main__':
    main()
