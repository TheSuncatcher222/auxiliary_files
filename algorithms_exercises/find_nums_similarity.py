"""
Дано два числа без ведущих нулей, разделенные пробельным символом. Необходимо
проверить, можно ли получить второе число (в т.ч. с ведущим нулем) из первого
перестановкой цифр.
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: str = '134 341'  # True
INPUT_2: str = '112 111'  # False
INPUT_3: str = '3 33'     # False

INPUT: str = INPUT_1

DIGITS: int = 10


def read_input() -> list:
    """Read input data and return 2 numbers"""
    return list(map(int, INPUT.split()))


def create_sorted_nums(num: int) -> list:
    """Sort nums by counting."""
    num_digits: list = [0] * DIGITS
    while num != 0:
        div_num = divmod(num, 10)
        num_digits[div_num[1]] += 1
        num = div_num[0]
    return num_digits


def main():
    x, y = read_input()
    x_digits: list = create_sorted_nums(x)
    y_digits: list = create_sorted_nums(y)
    print(all(x_digits[i] == y_digits[i] for i in range(DIGITS)))


if __name__ == '__main__':
    main()
