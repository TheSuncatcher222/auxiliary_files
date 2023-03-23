"""
Для каждой из строки (имя пользователя) в массиве вывести список символов,
которые не попадают под паттерн r'[\w.@+-]+', в единственном экземпляре.
"""

"""Примеры с ответами для тестов со всеми условиями."""
# Username '{, ,}' contains forbidden symbols: {' ', '{', ',', '}'}
INPUT_1: str = '{, ,}'
# Username must have one character at least!
INPUT_2: str = ''

INPUT: str = INPUT_1

from re import sub

PATTERN = r'[\w.@+-]+'


def main() -> str:
    forbidden_symbols: set = set(sub(PATTERN, '', INPUT))
    if forbidden_symbols:
        print(
            f"Username '{INPUT}' contains forbidden symbols: "
            f"{forbidden_symbols}")
    elif INPUT == '':
        print('Username must have one character at least!')
    else:
        print(f'Username "{INPUT}" is OK!')


if __name__ == '__main__':
    main()
