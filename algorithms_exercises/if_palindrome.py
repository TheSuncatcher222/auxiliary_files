"""
В единственной строке записана фраза, состоящая из строчных и прописных
латинских букв, цифр, знаков препинания.

Определите, является ли фраза палиндромом. Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.

Выведите True, если фраза является палиндромом и False, если не является.
"""

"""Примеры с ответами для тестов."""
INPUT_1: str = 'A man, a plan, a canal: Panama'  # True
INPUT_2: str = 'Ab'                              # False

INPUT: str = INPUT_1

from re import sub


def main():
    text = sub(r'\W', '', INPUT)
    i = 0
    j = len(text) - 1
    while i < j:
        if text[i].lower() != text[j].lower():
            print(False)
        i += 1
        j -= 1
    print(True)


if __name__ == '__main__':
    main()
