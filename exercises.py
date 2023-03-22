from decorators import time_measure_decorator

# Может быть оставлять комментарии, почему где-то так, а не иначе?
# Mock тесты?

"""???"""

# def get_input():
# 	return input(), input()


# def find_letter(text_1, text_2):
#     chars_1 = count_chars(text_1)
#     chars_2 = count_chars(text_2)
#     for char in chars_2:
#         if char not in chars_1 or chars_2[char] != chars_1[char]:
#             return char


# def count_chars(text):
#     char_dict = {}
#     for char in text:
#         if char not in char_dict:
#              char_dict[char] = 0
#         char_dict[char] += 1
#     return char_dict


# text_1, text_2 = get_input()
# print(find_letter(text_1, text_2))



# """Задача.
# Красотой строки назовем максимальное число идущих подряд одинаковых букв.
# В заданной строке допускается заменить не более k символов (имеется ввиду не
# поменять символы в строке местами, а заменить символ независимо от других).
# Выведите одно число — максимально возможную красоту строчки, которую возможно
# получить. В качестве исходных данных через пробельный символ указывается
# максимальное допустимое количество замен k и непустая строка, состоящая
# только из маленьких латинских букв (без пробелов)."""

# INPUT = '3 heltoh'

# def main():
#     changes, text = INPUT.split()
#     text_length = len(text)
#     changes = int(changes)
#     if changes >= text_length - 1:
#         return len(text)
#     chars = {}
#     #for char in input():
#     i = 0
#     for char in text:
#         if char not in chars:
#             chars[char] = []
#         chars[char].append(i)
#         i += 1
#     beauty = changes + 1
#     for char_indexes in chars.values():
#         if len(char_indexes) == 1:
#             continue
#         current_beauty = 1
#         index_spaces = []
#         for i in range(len(char_indexes) - 1):
#             index_spaces.append(char_indexes[i+1] - char_indexes[i] - 1)
#         delete_index = 0
#         for i in range(len(index_spaces)):
#             current_beauty += index_spaces[i] + 1
#             # if current_beauty > beauty:
#             #     beauty = current_beauty
#             if current_beauty <= changes

#             elif current_beauty > changes:
#                 current_beauty -+ index_spaces[delete_index]
#                 delete_index += 1
#         break


# main()
