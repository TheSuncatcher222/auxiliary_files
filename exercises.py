from decorators import time_measure_decorator

# Может быть оставлять комментарии, почему где-то так, а не иначе?
# Mock тесты?


"""
Дана строка S. Выведите гистограмму как в примере ниже (для "Hello world!"),
пробелы не учитываются, символы отсортированы в порядке увеличения кодов:
     #
     ##
#########
!,Hdelorw
"""

# INPUT = (
#     'Twas brillig, and the slithy toves\n'
#     'Did gyre and gimble in the wabe;\n'
#     'All mimsy were the borogoves,\n'
#     'And the mome raths outgrabe.')


# def main() -> str:
#     """Принимает текст и возвращает гистограмму использования символов."""
#     char_freq: dict[str, int] = {}
#     for char in INPUT:
#         if char not in char_freq:
#             char_freq[char] = 0
#         char_freq[char] += 1
#     # Быстрее пропускать символ в словарь, а потом удалить запись, чем
#     # проверять каждый символ на то, является ли он пробелом (при условии,
#     # что пробелов в основной массе не так много).
#     char_freq.pop(' ')
#     lines_count = max(char_freq.values())
#     text_lines = [''] * (lines_count + 1)
#     text_lines[0] += ''.join((char for char in sorted(char_freq)))
#     for key in sorted(char_freq):
#         for i in range(1, lines_count + 1):
#             if char_freq[key] >= i:
#                 text_lines[i] += '#'
#             else:
#                 text_lines[i] += ' '
#     text = '\n'.join(text_lines[i] for i in reversed(range(lines_count+1)))
#     print(text)


# if __name__ == '__main__':
#     main()

"""
Необходимо сгруппировать все приведенные слова по общим буквам и вывести
каждую группу на новой строке. Слова указываются только строчными буквами,
через пробел.
"""

# """Примеры с ответами для тестов."""
# INPUT_1: str = 'eat tea tan ate nat bat'  # ate eat tea \n nat tan n bat

# INPUT: str = INPUT_1


# def main():
#     words: str = INPUT.split()
#     groups: dict[str, str] = {}
#     for word in words:
#         word_sorted = ''.join(sorted(word))
#         if word_sorted not in groups:
#             groups[word_sorted] = []
#         groups[word_sorted].append(word)
#     for group in groups:
#         print(' '.join(word for word in groups[group]))


# if __name__ == '__main__':
#     main()

""""
Дана матрица. Для заданного элемента нужно вернуть список всех его
соседей в возрастающем порядке через пробел. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Например, для ячейки {0,0} соседями будут '0 2', для {2,1} - '1, 2, 7, 7'.
1 2 3
0 2 6
7 4 1
2 7 0

- В первой строке задано n — количество строк матрицы.
- Во второй — количество столбцов m. Числа m и n не превосходят 1000.
- В следующих n строках задана матрица. Элементы матрицы — целые числа, по
модулю не превосходящие 1000.
- В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.
"""

# INPUT1 = '4'
# INPUT2 = '3'
# INPUT3 = '1 2 3'
# INPUT4 = '0 2 6'
# INPUT5 = '7 4 1'
# INPUT6 = '2 7 0'
# # Правильный ответ для точки {0,0}: '0 2'
# INPUT7 = '0'
# INPUT8 = '0'


# def read_input() -> tuple:
#     """Read input data."""
#     rows = int(input())
#     cols = int(input())
#     matr = []
#     for row in range(rows):
#     	matr.append(list(map(int, input().split())))
#     i = int(input())
#     j = int(input())
#     return rows, cols, matr, i, j


# def find_result(rows, cols, matr, i, j):
#     result = []
#     if rows == 1:
#         pass
#     elif i == 0:
#         result.append(matr[i+1][j])
#     elif i == rows - 1:
#         result.append(matr[i-1][j])
#     else:
#         result.append(matr[i+1][j])
#         result.append(matr[i-1][j])
#     if cols == 1:
#         pass
#     elif j == 0:
#         result.append(matr[i][j + 1])
#     elif j == cols - 1:
#         result.append(matr[i][j - 1])
#     else:
#         result.append(matr[i][j + 1])
#         result.append(matr[i][j - 1])
#     result.sort()
#     return result


# rows, cols, matr, i, j = read_input()
# print(' '.join(map(str, find_result(rows, cols, matr, i, j))))

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

"""
Улица имеет длину n. Все участки на улице стоят в один ряд. Каждый участок
или пустой, или имеет построенный обитаемый дом.

Необходимо для каждого из участков указать расстояние до ближайшего пустого.
Если участок пустой, эта величина будет равна 0 - расстояние до самого себя.
Числа необходимо вывести в одну строку, разделяя пробелом.

Участки пронумерованы вразнобой с 1. Каждый пустой участок обозначается 0.
В первой строке дана длина улицы n (1 ≤ n ≤ 10^6). В следующей записаны n целых
неотрицательных чисел - номера домов и обозначение пустых участков.
Гарантируется, что в последовательности будет хотя бы один 0, а номера домов
являются целыми числами.

Например, для длины улицы 7 (0 1 5 4 9 0 2) ответ будет: 0 1 2 2 0 1
"""


# def get_input() -> tuple:
#     """Получает значение длины улицы и расположение домов в ряд на ней."""
#     street_len: int = int(input())
#     street: list = [int(_) for _ in input().split()]
#     return street_len, street


# def count_distance(street_len: int, street: list):
#     """Выводит список расстояний до ближайшего 0 для каждого из участков."""
#     result: list = [None] * street_len
#     max_index: int = street_len - 1
#     for plot_before_zero in range(street_len):
#         if street[plot_before_zero] != 0:
#             result[plot_before_zero] = max_index - plot_before_zero
#         else:
#             result[plot_before_zero] = 0
#             last_zero: int = plot_before_zero
#             break
#     if plot_before_zero == max_index:
#         return result
#     if plot_before_zero != 0:
#         dif: int = max_index - plot_before_zero
#         for plot_renew in range(plot_before_zero):
#             result[plot_renew] -= dif
#     i: int = 0
#     for plot in range(plot_before_zero + 1, street_len):
#         if street[plot] != 0:
#             i += 1
#             result[plot] = i
#         else:
#             result[plot] = 0
#             renew_value: int = 0
#             for plot_renew in range(plot - 1, (plot + last_zero) // 2, -1):
#                 renew_value += 1
#                 result[plot_renew] = renew_value
#             last_zero = plot
#             i = 0
#     return result


# def main():
#     street_len, street = get_input()
#     result: list = count_distance(street_len=street_len, street=street)
#     print(' '.join(map(str, result)))


# if __name__ == '__main__':
#     main()

"""
Предоставлено поле (кнопки) 4x4. В каждой ячейке указана либо точка, либо
цифра от 1 до 9. В каждый момент времени t (от 1 до 9) игрок должен
одновременно нажать на все кнопки, на которых указана цифра t. Если игрок
сумел нажать все необходимые кнопки - он получает 1 балл. Игрок может
одновременно нажать не более чем на k кнопок за раз.

Необходимо найти максимальное количество баллов, которое может может получить
игрок за игру для заданной конфигурации поля.

В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы кнопки строки - по 4 символа в каждой без
пробелов. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Например, для k = 3 и матрицы ниже ответ: 2
1 2 3 1
2 . . 2
2 . . 2
2 . . 2
"""

# GAMERS: int = 2
# FIELD_ROWS: int = 4
# ZERO_CHAR: str = '.'
# T = range(1, 9 + 1)


# def init_input() -> tuple:
#     """Получает значение k и количество символов на поле."""
#     max_nums_at_time: int = int(input()) * GAMERS
#     chars_count: dict[str, int] = {str(num): 0 for num in range(1, 10)}
#     chars_count['ZERO_CHAR'] = 0
#     for _ in range(FIELD_ROWS):
#         row: str = input()
#         for char in row:
#             if char != ZERO_CHAR:
#                 chars_count[char] += 1
#     return max_nums_at_time, chars_count


# def count_points(max_nums_at_time: int, chars_count: dict[str, int]) -> str:
#     """Вычисляет максимальное количество баллов."""
#     result: int = 0
#     for second in T:
#         if 0 < chars_count[str(second)] <= max_nums_at_time:
#             result += 1
#     return result


# def main():
#     max_nums_at_time, chars_count = init_input()
#     print(count_points(
#         max_nums_at_time=max_nums_at_time, chars_count=chars_count))


# if __name__ == '__main__':
#     main()

"""
Существуют наклейки, на которых указаны числа. У одного коллекционера есть N
наклеек, причем могут быть повторяющиеся. К нему пришли K людей, которые также
собирают наклейки и хотели бы пополнить свою коллекцию за счет коллекционера.

В первой строке ввода содержится число - количество наклеек коллекционера.
Во второй строке через запятую перечислены вразнобой числа - наклейки
коллекционера. В третьей строке - количество К людей. В четвертой строке указан
минимальный номер pi, с которого включительно для коллекционера №i карточки не
представляют интереса.

Одной строкой для каждого человека необходимо вывести количество карточек
коллекционера, которые представляют интерес.

Каждому человеку не интересно иметь 2 одинаковых карточек. Помимо этого сейчас
карточки не раздаются, цель - просто найти потенциально интересующие элементы
коллекции.
"""

# """Примеры с ответами для тестов."""
# INPUT_1: list = [
#     '1',
#     '5',
#     '2',
#     '4 5']  # 0 1
# INPUT_2: list = [
#     '7',
#     '100 1 50 50 100 50 0',
#     '3',
#     '300 0 75']  # 4 1 3

# INPUT: list = INPUT_2


# def read_input() -> tuple:
#     """Read input data."""
#     cards_quantity: int = int(INPUT[0])
#     cards: list = list(map(int, INPUT[1].split()))
#     peoples_quantity: int = int(INPUT[2])
#     cards_required: list = list(map(int, INPUT[3].split()))
#     return cards_quantity, cards, peoples_quantity, cards_required


# def count_requirements(
#         cards_quantity: int,
#         cards: list,
#         peoples_quantity: int,
#         peoples_required: list[list[int, int]]) -> dict:
#     answer: dict[int, int] = {i: 0 for i in range(peoples_quantity)}
#     current_people: int = 0
#     cards_available: int = 0
#     card_previous: int = -1
#     current_card_index: int = 0
#     while current_card_index < cards_quantity:
#         card: int = cards[current_card_index]
#         if card == card_previous:
#             current_card_index += 1
#         elif card <= peoples_required[current_people][1]:
#             cards_available += 1
#             current_card_index += 1
#             card_previous = card
#         else:
#             answer[peoples_required[current_people][0]] = cards_available
#             current_people += 1
#     answer[peoples_required[current_people][0]] = cards_available
#     return answer


# def main():
#     cards_quantity, cards, peoples_quantity, cards_required = read_input()
#     cards.sort()
#     peoples_required = []
#     for i in range(peoples_quantity):
#         peoples_required.append([i, cards_required[i]])
#     peoples_required = sorted(peoples_required, key=lambda people: people[1])
#     answer = count_requirements(
#         cards_quantity, cards, peoples_quantity, peoples_required)
#     print(' '.join(map(str, answer.values())))


# if __name__ == '__main__':
#     main()

"""
Количество учеников N пришло на контрольную. Все парты стоят в одну колонну.
Учитель подготовил K вариантов заданий. За каждой партой (кроме, возможно,
последней) будут находиться ровно 2 ученика. Варианты будут раздаваться строго
по порядку: левый ученик первой парты получит 1й вариант, правый ученик первой
парты второй, левый ученик второй парты получит 3й вариант (N > 2) и т.д.

Отличник вошел первый в класс и занял случайное место. Двоечник хочет получить
такой же вариант, как и отличник, и обязательно сидеть в ряду позади, а не
перед отличником, при этом занять место как можно ближе. 

В ответе через запятую укажите номер ряда и номер позиции за партой (1 - слева,
2 - справа), куда следует сесть двоечнику. Если такого места нет, укажите "-1".

В первой строке ввода находится количество учеников N. Во второй строке -
количество подготовленных вариантов работ K. В третьей строке - номер ряда,
куда сел отличник, в четвертой - положение за партой (1 - слева, 2 - справа).
"""

# """Примеры с ответами для тестов."""
# INPUT_1 = [  # 2 2
#     25,
#     2,
#     1,
#     2]
# INPUT_2 = [  # -1
#     25,
#     13,
#     7,
#     1]

# INPUT = INPUT_1


# def find_nearest_seat(
#         students_count: int,
#         exc_count: int,
#         lookup_row: int,
#         lookup_seat: int) -> str or int:
#     lookup_seat_num: int = lookup_seat + 2 * (lookup_row - 1)
#     lookup_exc: int = lookup_seat_num % exc_count
#     if lookup_exc == 0:
#         lookup_exc = exc_count
#     target_seat_nym: int = lookup_seat_num + exc_count
#     if target_seat_nym > students_count:
#         return -1
#     target_row_seat: tuple(int, int) = divmod(target_seat_nym, 2)
#     if target_row_seat[1] == 0:
#         result: str = f'{target_row_seat[0]} 2'
#     else:
#         result: str = f'{target_row_seat[0] + 1} 1'
#     return result


# def main():
#     students_count, exc_count, lookup_row, lookup_seat = INPUT
#     print(find_nearest_seat(
#         students_count=students_count,
#         exc_count=exc_count,
#         lookup_row=lookup_row,
#         lookup_seat=lookup_seat))


# if __name__ == '__main__':
#     main()

"""
Хаотичность погоды за n дней понимается количество дней, в которые
температура строго больше чем в день до (если существует) и в день после (если
существует).

Необходимо вывести единственным числом хаотичность погоды за данный период.
В первой строке ввода указывается количество дней, во второй - температуры.
Единственный день в периоде также является хаотичным.
"""

# """Примеры с ответами для тестов."""
# INPUT_1: list[str] = [  # 3
#     '7',
#     '-1 -10 -8 0 2 0 5'
# ]
# INPUT_2: list[str] = [  # 2
#     '5',
#     '1 2 5 4 8'
# ]
# INPUT_3: list[str] = [  # 1
#     '1',
#     '0'
# ]
# INPUT_4: list[str] = [  # 0
#     '5',
#     '1 1 1 1 1'
# ]
# INPUT_5: list[str] = [  # 0
#     '5',
#     '1 1 0 1 1'
# ]

# INPUT: list[str] = INPUT_1


# def read_input() -> tuple[int, list[int]]:
#     """Read input data"""
#     cnt_days: int = int(INPUT[0])
#     temps: list[int] = list(map(int, INPUT[1].split()))
#     return cnt_days, temps


# def count_chaos(cnt_days: int, temps: list[int]):
#     """Count temperature chaos in given period."""
#     if cnt_days == 1:
#         return 1
#     elif cnt_days == 2:
#         if temps[0] != temps[1]:
#             return 1
#         return 0
#     result: int = 0
#     if temps[0] > temps[1]:
#         result += 1
#     for day_index in range(1, cnt_days - 1):
#         if (temps[day_index] > temps[day_index - 1]
#                 and temps[day_index] > temps[day_index + 1]):
#             result += 1
#     if temps[cnt_days - 1] > temps[cnt_days - 2]:
#         result += 1
#     return result


# def main():
#     cnt_days, temps = read_input()
#     print(count_chaos(cnt_days, temps))


# if __name__ == '__main__':
#     main()

"""
Узник замка проделал в стене прямоугольное отверстие DxE. Замок сделан из
прямоугольных кирпичей размеров AxBxC каждый.

Для заданных A, B, C, D, E напишите True, если кирпич пройдет в отверстие и
False - если нет. Все параметры представлены натуральными числами и указаны
через пробел.
"""

# """Примеры с ответами для тестов."""
# INPUT_1 = '10 20 20 20 10'  # True
# INPUT_2 = '10 20 20 10 10'  # False

# INPUT = INPUT_1

# from sys import exit

# def sort_two(first, second):
#     if first > second:
#         return second, first
#     return first, second

# def main():
#     a, b, c, d, e = list(map(int, INPUT.split()))
#     a, b = sort_two(a, b)
#     b, c = sort_two(b, c)
#     a, b = sort_two(a, b)
#     d, e = sort_two(d, e)
#     if a <= d and b <= e:
#         print(True)
#         exit()
#     print(False)


# if __name__ == '__main__':
#     main()


"""
Для указанной последовательности чисел от 0 до 9, разделенных пробелом,
необходимо определить, какое минимальное количество и каких чисел надо
приписать в конец этой последовательности, чтобы она стала симметричной.

В первой строке ответа укажите количество, а во второй приведите через пробел
сами приписываемые числа в том порядке, в каком их надо добавить.
"""

# """Примеры с ответами для тестов."""
# INPUT_1: str = '1 3 8 9 4 4 9'                 # 3 \n 8 3 1
# INPUT_2: str = '1 3 8 9 4 3 1 4 9'             # 8 \n 4 1 3 4 9 8 3 1
# INPUT_3: str = '1 1 1 1 1 1 1 1'               # 0 \n
# INPUT_4: str = '1 2 1 3 1 2 1 4 1 2 1 3 1'     # 2 \т 2 1

# INPUT: str = INPUT_4


# def main():
#     ans: list = [str]
#     nums: list[str] = INPUT.split()
#     nums_len: int = len(nums)
#     for left in range(nums_len - 1):
#         left_fix: int = left
#         right: int = nums_len - 1
#         while nums[left] == nums[right] and left <= right:
#             left += 1
#             right -= 1
#         if left > right:
#             break
#         else:
#             ans.insert(0, nums[left_fix])
#     NL: str = '\n'
#     print(f"{len(ans)}{NL}{' '.join(ans)}")


# if __name__ == '__main__':
#     main()
























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
