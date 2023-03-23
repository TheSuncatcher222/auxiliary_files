"""
Дана строка S. Выведите гистограмму как в примере ниже (для "Hello world!"),
пробелы не учитываются, символы отсортированы в порядке увеличения кодов:
     #
     ##
#########
!,Hdelorw
"""

"""Примеры с ответами для тестов."""
INPUT_1: str = 'Hello world!'
INPUT_2: str = (
    'Twas brillig, and the slithy toves\n'
    'Did gyre and gimble in the wabe;\n'
    'All mimsy were the borogoves,\n'
    'And the mome raths outgrabe.')

INPUT: str = INPUT_2


def main() -> str:
    """Принимает текст и возвращает гистограмму использования символов."""
    char_freq: dict[str, int] = {' ': 0, '\n': 0}
    for char in INPUT:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
    # Быстрее пропускать символ в словарь, а потом удалить запись, чем
    # проверять каждый символ на то, является ли он пробелом (при условии,
    # что пробелов в основной массе не так много).
    char_freq.pop(' ')
    char_freq.pop('\n')
    lines_count: int = max(char_freq.values())
    text_lines: list[str] = [''] * (lines_count + 1)
    text_lines[0] = ''.join((char for char in sorted(char_freq)))
    for key in sorted(char_freq):
        for i in range(1, lines_count + 1):
            if char_freq[key] >= i:
                text_lines[i] += '#'
            else:
                text_lines[i] += ' '
    print('\n'.join(text_lines[i] for i in reversed(range(lines_count+1))))


if __name__ == '__main__':
    main()
