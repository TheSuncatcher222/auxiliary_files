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

"""Примеры с ответами для тестов."""
INPUT_1: list[int] = [  # 2 2
    25,
    2,
    1,
    2]
INPUT_2: list[int] = [  # -1
    25,
    13,
    7,
    1]

INPUT: list[int] = INPUT_1


def find_nearest_seat(
        students_count: int,
        exc_count: int,
        lookup_row: int,
        lookup_seat: int) -> str or int:
    """Find nearest seat."""
    lookup_seat_num: int = lookup_seat + 2 * (lookup_row - 1)
    lookup_exc: int = lookup_seat_num % exc_count
    if lookup_exc == 0:
        lookup_exc = exc_count
    target_seat_nym: int = lookup_seat_num + exc_count
    if target_seat_nym > students_count:
        return -1
    target_row_seat: tuple(int, int) = divmod(target_seat_nym, 2)
    if target_row_seat[1] == 0:
        result: str = f'{target_row_seat[0]} 2'
    else:
        result: str = f'{target_row_seat[0] + 1} 1'
    return result


def main():
    students_count, exc_count, lookup_row, lookup_seat = INPUT
    print(find_nearest_seat(
        students_count=students_count,
        exc_count=exc_count,
        lookup_row=lookup_row,
        lookup_seat=lookup_seat))


if __name__ == '__main__':
    main()
