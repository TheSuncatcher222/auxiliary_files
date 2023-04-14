"""
На схеме земельного участка обозначены клумбы: горизонтальными отрезками,
лежащими на одной прямой. Каждая клумба обрабатывается отдельным садовником.

Процесс организации работ был выстроен плохо, так как одна и та же клумба (или
ее часть) могла быть обработана несколькими садовниками. Таким образом, клумбы
(отрезки) могли сливаться в одну (один). Нужно определить границы каждой
отдельной клумбы после производства работ.

Например, даны 4 отрезка [7,8], [7,8], [2,3], [6 10]:
1) два одинаковых отрезка [7,8] сольются в один;
2) отрезок [8,10] пересекается с отрезком [7,8] и получается [7,10];
3) отрезок [2,3] не пересекается с [7,10].
4) таким образом, получается два отрезка: [2,3] и [7,10].

В первой строке ввода задано количество n садовников, а в последующих n
строках - их земельные участки: координата начала start и конца end.
Start всегда строго меньше end.

"""

INPUT_1: list[int, str] = [
    4,
    '7 8',  # 2 3
    '7 8',  # 6 10
    '2 3',
    '6 10']
INPUT_2: list[int, str] = [
    13,
    '73 99',  # 1 99
    '2 43',
    '24 75',
    '11 80',
    '1 46',
    '29 45',
    '51 68',
    '64 92',
    '7 81',
    '36 63',
    '7 81',
    '36 63',
    '80 97',
    '29 92',
    '61 69']

INPUT: list[int, str] = INPUT_1

"""Эффективна при элементах больше ~90.
Иначе рекомендуется сортировка перестановками."""
def sort_arrow(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    index_mid = arr_len // 2
    arr_left = sort_arrow(arr[:index_mid])
    arr_right = sort_arrow(arr[index_mid:])
    index_left = index_right = 0
    merge_result = []
    while index_left < len(arr_left) and index_right < len(arr_right):
        if arr_left[index_left][0] <= arr_right[index_right][0]:
            merge_result.append(arr_left[index_left])
            index_left += 1
        else:
            merge_result.append(arr_right[index_right])
            index_right += 1
    merge_result += arr_left[index_left:]
    merge_result += arr_right[index_right:]
    for i in range(arr_len):
        arr[i] = merge_result[i]
    return arr


def union_arrow(arrow, len_arrow):
    start, end = arrow[0]
    for i in range(1, len_arrow):
        start_new = arrow[i][0]
        end_new = arrow[i][1]
        if start_new <= end:
            end = max(end, end_new)
        else:
            print(f'{start} {end}')
            start, end = start_new, end_new
    print(f'{start} {end}')


def main():
    n = INPUT[0]
    lands = [None] * n
    for i in range(n):
        lands[i] = list(map(int, INPUT[i+1].split()))
    sort_arrow(lands)
    union_arrow(lands, n)


if __name__ == '__main__':
    main()
