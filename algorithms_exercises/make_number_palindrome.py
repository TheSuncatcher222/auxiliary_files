"""
Для указанной последовательности чисел от 0 до 9, разделенных пробелом,
необходимо определить, какое минимальное количество и каких чисел надо
приписать в конец этой последовательности, чтобы она стала симметричной.

В первой строке ответа укажите количество, а во второй приведите через пробел
сами приписываемые числа в том порядке, в каком их надо добавить.
"""

"""Примеры с ответами для тестов."""
INPUT_1: str = '1 3 8 9 4 4 9'                 # 3 \n 8 3 1
INPUT_2: str = '1 3 8 9 4 3 1 4 9'             # 8 \n 4 1 3 4 9 8 3 1
INPUT_3: str = '1 1 1 1 1 1 1 1'               # 0 \n
INPUT_4: str = '1 2 1 3 1 2 1 4 1 2 1 3 1'     # 2 \т 2 1

INPUT: str = INPUT_1


def main():
    ans: list = []
    nums: list[str] = INPUT.split()
    nums_len: int = len(nums)
    for left in range(nums_len - 1):
        left_fix: int = left
        right: int = nums_len - 1
        while nums[left] == nums[right] and left <= right:
            left += 1
            right -= 1
        if left > right:
            break
        else:
            ans.append(nums[left_fix])
    ans.reverse()
    NL: str = '\n'
    print(f"{len(ans)}{NL}{' '.join(ans)}")


if __name__ == '__main__':
    main()
