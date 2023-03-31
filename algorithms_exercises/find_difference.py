"""
Дана отсортированная последовательность N чисел и число K. Необходимо найти
количество пар чисел таких, что B - A > K.
В первой строке ввода указано число K, во второй приведена последовательность.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[str] = [  # 6
    '3',
    '1 2 3 4 5 6 7']
INPUT_2: list[str] = [  # 3
    '4',
    '1 3 5 7 8']


INPUT: list[str] = INPUT_2


def main():
    k: int = int(INPUT[0])
    nums: list[int] = list(map(int, INPUT[1].split()))
    len_nums: int = len(nums)
    pairs: int = 0
    i: int = 0
    j: int = 1
    while j < len_nums:
        result = nums[j] - nums[i]
        if result <= k:
            j += 1
        else:
            pairs += len_nums - j
            i += 1
    print(pairs)


if __name__ == '__main__':
    main()
