"""
В списке из n целых чисел, указанных через пробел, найдите такие три числа,
произведение которых максимально. Решение должно иметь сложность O(n).
Применять сортировку к последовательности запрещено.
Числа допускается вывести в любом порядке через пробел."""

"""Примеры с ответами для тестов."""
INPUT_1: str = '1 4 2 4 5 -1 -2 -10'  # -10 -2 5
INPUT_2: str = '0 0 0 0 0'            # 0 0 0
INPUT_3: str = '3 1 2'                # 1 2 3
INPUT_4: str = '-1000 1 2 100'        # 1 2 100
INPUT_5: str = '-100 2 1000 -1'       # -100 -1 1000

INPUT: str = INPUT_1

from functools import reduce


def main():
    nums: list[int] = list(map(int, INPUT.split()))
    ans_negative: list[int] = nums[:3]
    ans_negative.sort()
    ans_positive: list[int] = nums[:3]
    for num_index in range(3, len(nums)):
        current_num = nums[num_index]
        if current_num > ans_positive[2]:
            ans_positive[0], ans_positive[1], ans_positive[2] = (
                ans_positive[1], ans_positive[2], current_num)
            ans_negative[2] = current_num
        elif current_num > ans_positive[1]:
            ans_positive[0], ans_positive[1] = ans_positive[1], current_num
        elif current_num > ans_positive[0]:
            ans_positive[0] = current_num
        if current_num < ans_negative[0]:
            ans_negative[1], ans_negative[0] = ans_negative[0], current_num
        elif current_num < ans_negative[1]:
            ans_negative[1] = current_num
    ans_positive_res = reduce(lambda i, j: i * j, ans_positive)
    ans_negative_res = reduce(lambda i, j: i * j, ans_negative)
    if ans_positive_res >= ans_negative_res:
        print(*ans_positive)
    else:
        print(*ans_negative)


if __name__ == '__main__':
    main()
