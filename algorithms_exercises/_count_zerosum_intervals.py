"""
Дана последовательность N чисел. Необходимо найти количество отрезков с
нулевой суммой."""

"""Примеры с ответами для тестов."""
#               0 1 1  1 -3  2 -3 -3 2 
INPUT_1: str = '1 0 0 -4  5 -5  0  5'  # 4 
#                 0 0
#                        5 -5
#                        5 -5  0
#                          -5  0 -5
INPUT_2: str = '-1 0 0 -4 5 -5 0 5'  # 6
#               -1 0 0 -4 5
#               -1 0 0 -4 5 -5 0 5
#                  0 0
#                         5 -5
#                         5 -5 0
#                           -5 0 5
INPUT_3: str = '-1 0 0 1 5 -5 0 5'  # 7
#               -1 0 0 1
#               -1 0 0 1 5 -5
#               -1 0 0 1 5 -5 0
#                  0 0
#                        5 -5
#                        5 -5 0
#                          -5 0 5
INPUT_4: str = '1'  # 0

INPUT: str = INPUT_1

# https://youtu.be/de28y8Dcvkg?list=PL6Wui14DvQPySdPv5NUqV3i8sDbHkCKC5&t=1262
def main_n_1():
    nums: list[int] = list(map(int, INPUT.split()))
    n: int = len(nums)
    prefix_sums: dict[int, int] = {0: 1}
    current_sum = 0
    for i in range(n):
        current_sum += nums[i]
        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = 0
        prefix_sums[current_sum] += 1
    print(prefix_sums)
    count_zero_intervals: int = 0
    for sum in prefix_sums:
        k = prefix_sums[sum]
        count_zero_intervals += (k * (k - 1)) // 2
    print(count_zero_intervals)


def main_n_2():
    nums: list[int] = list(map(int, INPUT.split()))
    n: int = len(nums)
    count_zero_intervals: int = 0
    for i in range (n - 1):
        range_sum: int = nums[i]
        for j in range(i + 1, n):
            range_sum += nums[j]
            if range_sum == 0:
                count_zero_intervals += 1
    print(count_zero_intervals)


if __name__ == '__main__':
    main_n_1()
    main_n_2()
