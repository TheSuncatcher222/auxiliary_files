"""
Для заданной последовательности буквенных символов без пробелов вывести строку
к виду: символ-количество-символ-количество-сим...
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: str = 'AAABCDD'  # A3BCD2
INPUT_2: str = 'Z'        # Z
INPUT_3: str = 'XX'       # X2

INPUT: str = INPUT_1


def main():
    result: list = []
    char_fixed: str = INPUT[0]
    char_count: int = 0
    for char_current in INPUT:
        if char_current == char_fixed:
            char_count += 1
        else:
            if char_count == 1:
                result.append(char_fixed)
            else:
                result.append(f'{char_fixed}{char_count}')
            char_count = 1
            char_fixed = char_current
    if char_count == 1:
        result.append(char_fixed)
    else:
        result.append(f'{char_fixed}{char_count}')
    print(''.join(result))


if __name__ == '__main__':
    main()
