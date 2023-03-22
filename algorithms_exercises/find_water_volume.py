"""
Двухмерный остров состоит из столбцов различной высоты. Над островом прошел
дождь и заполнил водой все низины, а не поместившаяся вода утекла в море, не
увеличив его уровень. По ландшафту острова определите, сколько блоков воды
суммарно осталось в низинах. Ответ выведите одним числом.
"""

"""Примеры с ответами для тестов:
Для острова '3 1 4 3 5 1 1 2 5 1 1 4 3 2 1' ответ будет 20.
    #///#
  #/#///#//#
#/###///#//##
#/###//##//###
###############
"""

INPUT_1 = '3 1 4 3 5 1 1 3 1'              # 7
INPUT_2 = '3 1 4 3 5 1 1 2 5 1 1 4 3 2 1'  # 20
INPUT_3 = '5 1 5'                          # 4
INPUT_4 = '1 2 1'                          # 0
INPUT_5 = '1 1 1'                          # 0
INPUT_6 = '3 2 1'                          # 0
INPUT_7 = '1 2 3'                          # 0

INPUT: str = INPUT_1


def read_input() -> list:
    """Read input data."""
    alts: list = list(map(int, INPUT.split()))
    return alts


def get_max_alt_indexes(alts: list) -> tuple:
    """Get indexes for max values in island altitudes."""
    max_alt: int = 0
    max_alt_index: list = []
    for i in range(len(alts)):
        if alts[i] > max_alt:
            max_alt = alts[i]
            max_alt_index = [i]
        elif alts[i] == max_alt:
            max_alt_index.append(i)
    return max_alt_index


def count_vol_edge(alts: list, max_alt: int, range: range) -> int:
    """Count water volume on islands edge (before first maximum altitude)."""
    volume: int = 0
    for i in range:
        alt: int = alts[i]
        if alt < max_alt:
            volume += max_alt - alt
        elif alt > max_alt:
            max_alt = alt
    return volume


def count_vol_mid(alts: list, left_max: int, right_max: int) -> int:
    """Count water volume between maximum altitudes."""
    # It's a bit faster than: volume = 0 -> volume += max_alt - alts[i]
    volume = alts[left_max] * (right_max - left_max - 1)
    for alt in range(left_max + 1, right_max):
        volume -= alts[alt]
    return volume


def main():
    alts: list = read_input()
    max_alt_index: list = get_max_alt_indexes(alts=alts)
    vol_left: int = 0
    vol_mid: int = 0
    vol_right: int = 0
    if len(max_alt_index) != 1:
        for i in range(len(max_alt_index) - 1):
            vol_mid += count_vol_mid(
                alts=alts,
                left_max=max_alt_index[i],
                right_max=max_alt_index[i+1])
    if max_alt_index[0] != 0:
        vol_left = count_vol_edge(
            alts=alts, max_alt=alts[0], range=range(max_alt_index[0] + 1))
    if max_alt_index[-1] != len(alts):
        vol_right = count_vol_edge(
            alts=alts,
            max_alt=alts[len(alts)-1],
            range=range(len(alts)-1, max_alt_index[-1], -1))
    print(vol_left + vol_mid + vol_right)


if __name__ == '__main__':
    main()
