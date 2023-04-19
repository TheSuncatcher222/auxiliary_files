"""
Вася пригласил в гости N своих одноклассников. Мама Васи изготовила M печенья.
При этом печенье может быть разного размера. А у каждого ребенка есть фактор
жадности: минимальный размер печенья, который он возьмет.

Нужно выяснить, сколько детей останется останутся довольными в случае, если
каждый ребенок действует оптимально, а также не берет более одного печенья.

В первой строке указано число детей N
Во второй - N чисел, разделенных пробелом, являющихся фактором жадности.
В третьей - число M - количество печенья.
В четвертой - M чисел, разделенных пробелом, являющихся размером печенья.

Фактор жадности и размер печенья не превышают 1000.
"""

INPUT_1: list[int, str] = [  # 5
    10,
    '8 5 5 8 6 9 8 2 4 7',
    8,
    '9 8 1 1 1 5 10 8']

INPUT_2: list[int, str] = [  # 43
    50,
    ('39 82 14 63 46 7 63 44 2 50 91 17 75 28 78 9 45 66 77 82 90 68 48 19 64 '
     '63 12 77 75 84 10 86 39 62 34 18 22 95 43 58 89 61 64 11 91 2 23 31 12 '
     '49'),
    46,
    ('22 72 2 39 82 69 61 95 90 53 80 96 13 63 49 55 21 41 8 99 16 4 24 96 69 '
     '91 55 13 58 97 72 69 6 84 73 5 43 52 41 7 22 70 21 74 64 26')]

INPUT: list[int, str] = INPUT_1

"""
При установленном значении максимальной жадности и размера печенья
рекомендуется использовать сортировку подсчетом.
"""


def main_count_sort():
    MAX_INDEX = 1000 + 1
    _ = INPUT[0]
    kids_greed = [0] * MAX_INDEX
    for greed in list(map(int, INPUT[1].split())):
        kids_greed[greed] += 1
    _ = INPUT[2]
    cookies_size = [0] * MAX_INDEX
    for size in list(map(int, INPUT[3].split())):
        cookies_size[size] += 1
    greed = size = 1
    result = 0
    """
    Использование while greed < len(kids_greed) and size < len(cookies_size)
    приведет к замедлению программы на 5%"""
    try:
        while 1:
            if kids_greed[greed] == 0:
                greed += 1
            elif size < greed or cookies_size[size] == 0:
                size += 1
            else:
                result += 1
                kids_greed[greed] -= 1
                cookies_size[size] -= 1
    except IndexError:
        print(result)


"""
При неизвестном значении максимальной жадности и размера печенья рекомендуется
использовать быструю сортировку.
"""


def main_quick_sort():

    def __quick_sort(arr, left, right):
        if left >= right:
            return
        pivot = arr[(left + right) // 2]
        i = left - 1
        j = right + 1
        while 1:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        __quick_sort(arr, left, j)
        __quick_sort(arr, j+1, right)

    count_kids = INPUT[0]
    kids_greed = list(map(int, INPUT[1].split()))
    count_cookies = INPUT[2]
    cookies_size = list(map(int, INPUT[3].split()))
    __quick_sort(kids_greed, 0, count_kids-1)
    __quick_sort(cookies_size, 0, count_cookies-1)
    result = 0
    i = j = 0
    while i < count_kids and j < count_cookies:
        if kids_greed[i] <= cookies_size[j]:
            i += 1
            result += 1
        j += 1
    print(result)


main_count_sort()
main_quick_sort()
