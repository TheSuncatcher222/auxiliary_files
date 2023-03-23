"""
Необходимо сгруппировать все приведенные слова по общим буквам и вывести
каждую группу на новой строке. Слова указываются только строчными буквами,
через пробел.
"""

"""Примеры с ответами для тестов."""
INPUT_1: str = 'eat tea tan ate nat bat'  # ate eat tea \n nat tan n bat

INPUT: str = INPUT_1


def main():
    words: str = INPUT.split()
    groups: dict[str, str] = {}
    for word in words:
        word_sorted = ''.join(sorted(word))
        if word_sorted not in groups:
            groups[word_sorted] = []
        groups[word_sorted].append(word)
    for group in groups:
        print(*groups[group])


if __name__ == '__main__':
    main()
