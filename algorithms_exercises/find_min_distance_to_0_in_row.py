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

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: list[int, str] = [7, '0 1 5 4 9 0 2']  # 0 1 2 2 0 1
INPUT_2: list[int, str] = [7, '0 0 0 0 0 0 0']  # 0 0 0 0 0 0 0
INPUT_3: list[int, str] = [5, '0 1 1 1 1']      # 0 1 2 3 4
INPUT_4: list[int, str] = [5, '1 1 1 1 0']      # 4 3 2 1 0
INPUT_5: list[int, str] = [1, '0']              # 0

INPUT: list[int, str] = INPUT_1


def get_input() -> tuple:
    """Get input data."""
    street_len: int = INPUT[0]
    street: list = [int(_) for _ in INPUT[1].split()]
    return street_len, street


def count_distance(street_len: int, street: list):
    """Find list of distance to nearest 0 for each plot."""
    result: list = [None] * street_len
    max_index: int = street_len - 1
    for plot_before_zero in range(street_len):
        if street[plot_before_zero] != 0:
            result[plot_before_zero] = max_index - plot_before_zero
        else:
            result[plot_before_zero] = 0
            last_zero: int = plot_before_zero
            break
    if plot_before_zero == max_index:
        return result
    if plot_before_zero != 0:
        dif: int = max_index - plot_before_zero
        for plot_renew in range(plot_before_zero):
            result[plot_renew] -= dif
    i: int = 0
    for plot in range(plot_before_zero + 1, street_len):
        if street[plot] != 0:
            i += 1
            result[plot] = i
        else:
            result[plot] = 0
            renew_value: int = 0
            for plot_renew in range(plot - 1, (plot + last_zero) // 2, -1):
                renew_value += 1
                result[plot_renew] = renew_value
            last_zero = plot
            i = 0
    return result


def main():
    street_len, street = get_input()
    result: list = count_distance(street_len=street_len, street=street)
    print(*result)


if __name__ == '__main__':
    main()
