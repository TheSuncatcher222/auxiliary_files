"""
Разложите число на произведение простых множителей.
"""

"""Примеры с ответами для тестов."""
INPUT_1 = 8          # 2 2 2
INPUT_2 = 13         # 13
INPUT_3 = 88         # 2 2 2 11
INPUT_4 = 749        # 7 107
INPUT_5 = 862399     # 862399
INPUT_6 = 802066951  # 7 4951 23143

INPUT = INPUT_1


def main():
    num: int = int(INPUT)
    answer: list = []
    i: int = 2
    while i * i <= num:
        result = divmod(num, i)
        if result[1] == 0:
            answer.append(i)
            num //= i
        else:
            i += 1
    if num > 1:
        answer.append(num)
    print(*answer)


if __name__ == '__main__':
    main()
