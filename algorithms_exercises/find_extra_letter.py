"""
Даны две последовательности символов. Вторая отличается от первой наличием
одного дополнительного символа. Выведите этот символ.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[str] = [
    'fda14jriaf23df43kj',
    'fda14jriaf223df43kj']
INPUT_2: list[str] = [
    'aaaa',
    'aaaaa']
INPUT_3: list[str] = [
    'aaaa',
    'aaba']

INPUT: list[str] = INPUT_1


def count_chars(text):
    """Count chars by counting."""
    char_dict: dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict


def find_char(text_1, text_2):
    """Find extra char."""
    chars_1: dict[str, int] = count_chars(text_1)
    chars_2: dict[str, int] = count_chars(text_2)
    for char in chars_2:
        if char not in chars_1 or chars_2[char] != chars_1[char]:
            return char


def main():
    text_1, text_2 = INPUT
    print(find_char(text_1=text_1, text_2=text_2))


if __name__ == '__main__':
    main()
