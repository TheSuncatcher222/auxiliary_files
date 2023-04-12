"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:
2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'
Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий, в одну строку.
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: str = '23'  # ad ae af bd be bf cd ce cf
INPUT_2: str = '92'  # wa wb wc xa xb xc ya yb yc za zb zc

KEYBOARD: list[str] = [
    None,
    None,
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']]

INPUT: str = INPUT_1


def press_comb(
        nums: str, index: int = 0, result: str = '', result_list: list = []):
    """Compose combinations using recursion."""
    for letter in KEYBOARD[int(nums[index])]:
        if index + 1 < len(nums):
            press_comb(nums, index+1, result+letter, result_list)
        else:
            result_list.append(result + letter)
    return result_list


def main():
    result_list = press_comb(INPUT)
    print(' '.join(result_list))


if __name__ == '__main__':
    main()
