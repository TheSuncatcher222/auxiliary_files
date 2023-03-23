"""
Красотой строки назовем максимальное число идущих подряд одинаковых букв.
В заданной строке допускается заменить не более k символов (имеется ввиду не
поменять символы в строке местами, а заменить символ независимо от других).
Выведите одно число — максимально возможную красоту строчки, которую возможно
получить. В качестве исходных данных через пробельный символ указывается
максимальное допустимое количество замен k и непустая строка, состоящая
только из маленьких латинских букв (без пробелов)."""

INPUT = '3 heltoh'

def main():
    changes, text = INPUT.split()
    text_length = len(text)
    changes = int(changes)
    if changes >= text_length - 1:
        return len(text)
    chars = {}
    #for char in input():
    i = 0
    for char in text:
        if char not in chars:
            chars[char] = []
        chars[char].append(i)
        i += 1
    beauty = changes + 1
    for char_indexes in chars.values():
        if len(char_indexes) == 1:
            continue
        current_beauty = 1
        index_spaces = []
        for i in range(len(char_indexes) - 1):
            index_spaces.append(char_indexes[i+1] - char_indexes[i] - 1)
        delete_index = 0
        for i in range(len(index_spaces)):
            current_beauty += index_spaces[i] + 1
            # if current_beauty > beauty:
            #     beauty = current_beauty
            if current_beauty <= changes:
                pass
            elif current_beauty > changes:
                current_beauty -+ index_spaces[delete_index]
                delete_index += 1
        break


main()
