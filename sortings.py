def is_val1_less_val2(val_1: any, val_2: any, key: any = None) -> bool:
    """Компаратор.
    Возвращает итог сравнения двух значений:
        - тип integer/float:
            - True, если value_1 меньше, чем value_2
            - False, если value_1 больше или равно value_2
        - тип ..."""
    if type(val_1) in (int, float) and type(val_2) in (int, float):
        return val_1 < val_2
    if isinstance(val_1, str) and isinstance(val_2, str):
        return val_1 < val_2
    raise TypeError(
        'Функция "comparator" не умеет сравнивать такие типы данных: '
        f'{type(val_1)} (val_1) и {type(val_2)} (val_2).')


def sort_insertion(arr: list[int]) -> list[int | float]:
    """Реализует сортировку вставками.
    Принимает неотсортированный массив, возвращает отсортированный.
    Сложность по времени: O(n²).
    Сложность по памяти: O(1).
    Устойчивость: ДА."""
    if '__iter__' not in dir(arr):
        return TypeError('В функцию сообщен не итерируемый объект!')
    for i in range(1, len(arr)):
        item_to_insert: int = arr[i]
        j: int = i
        while j > 0 and arr[j-1] > item_to_insert:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


print(sort_insertion([11, 2, 9, 7, 1]))


def sort_insertion_comparator(arr: list[int | float]) -> list[int | float]:
    """Реализует сортировку вставками с использованием компаратора.
    Принимает неотсортированный массив, возвращает отсортированный.
    Сложность по времени: O(n²).
    Сложность по памяти: O(1).
    Устойчивость: ДА."""
    if '__iter__' not in dir(arr):
        return TypeError('В функцию сообщен не итерируемый объект!')
    for i in range(1, len(arr)):
        item_to_insert: int = arr[i]
        j: int = i
        while j > 0 and is_val1_less_val2(
                val_1=item_to_insert, val_2=arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


print(sort_insertion_comparator([11, 2, 9, 7, 1]))


def sort_merge(arr: list[int | float]) -> list[int | float]:
    """Реализует сортировку слиянием.
    Принимает неотсортированный массив, возвращает отсортированный.
    Сложность по времени: O(n∙log(n)).
    Сложность по памяти: O(n).
    Устойчивость: ДА."""
    if len(arr) <= 1:
        return arr
    index_mid: int = len(arr) // 2
    arr_left: list[int] = sort_merge(arr=arr[:index_mid])
    arr_right: list[int] = sort_merge(arr=arr[index_mid:])
    result: list = [None] * len(arr)
    index_left = index_right = index_result = 0
    while index_left < len(arr_left) and index_right < len(arr_right):
        if arr_left[index_left] <= arr_right[index_right]:
            result[index_result] = arr_left[index_left]
            index_left += 1
        else:
            result[index_result] = arr_right[index_right]
            index_right += 1
        index_result += 1
    if index_left == len(arr_left):
        while index_right < len(arr_right):
            result[index_result] = arr_right[index_right]
            index_right += 1
            index_result += 1
    else:
        while index_left < len(arr_left):
            result[index_result] = arr_left[index_left]
            index_left += 1
            index_result += 1
    return result


print(sort_merge([11, 2, 9, 7, 1]))


def sort_quick_optimized(arr: list[int]) -> list[int]:
    """Реализует оптимизированную быструю сортировку. Опорный элемент
    выбирается случайным образом: берется элемент по середине.
    Принимает неотсортированный массив, возвращает отсортированный.
    Сложность по времени: O(n∙log(n)) или O(n²) в худшем случае.
    Сложность по памяти: O(1).
    Устойчивость: ДА."""

    def _run_sort(arr: list[int], left: int, right: int) -> list[int]:
        if left >= right:
            return arr
        pivot: int = arr[(left+right)//2]
        left_index: int = left
        right_index: int = right
        while left_index <= right_index:
            if pivot > arr[left_index]:
                left_index += 1
            elif pivot < arr[right_index]:
                right_index -= 1
            else:
                arr[left_index], arr[right_index] = (
                    arr[right_index], arr[left_index])
                left_index += 1
                right_index -= 1
        _run_sort(arr=arr, left=left, right=left_index-1)
        _run_sort(arr=arr, left=left_index, right=right_index)
        return

    _run_sort(arr=arr, left=0, right=len(arr)-1)
    return arr


print(sort_quick_optimized([11, 2, 9, 7, 1]))
