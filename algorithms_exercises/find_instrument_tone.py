"""
Музыкант приобрел себе музыкальный инструмент треугольник. У музыканта есть
поверенный музыкальный тюнер, с помощью которого можно проигрывать ноту
любой частоты. При помощи тюнера музыкант хочет узнать, какой частоты его
треугольник. Для этого он включает на тюнере ноты с разными частотами и на слух
определяет, ближе она или дальше к издаваемому звуку, чем предыдущая нота.
Поскольку слух у музыканта абсолютный, заключения всегда абсолютно верны.

Музыкант предоставил запись с последовательностью частот, выставляемых им на
тюнере. Про каждую ноту, начиная со второй указано - ближе или дальше она к
звуку треугольника.

Заранее известно, что нота треугольника не менее 30 Гц и не более 4000 Гц.

Требуется указать наиболее точный интервал, на котором находится частота
звучания треугольника.
"""

"""Примеры с ответами для тестов."""
INPUT_1: list[str] = [                     # 225 275 (например, 125)
    '300 250 200 150 100',
    '      1   0   0   0']
INPUT_2: list[str] = [                     # 310 4000 (например, 3000)
    '240 260 280 300 320',
    '      1   1   1   1']
INPUT_3: list[str] = [                     # 1600 1900 (например, 1800)
    '1500 1700 2100 3900 3800',
    '        1   0     0    1']

INPUT: list[str] = INPUT_1

MIN_FREQ: int = 30
MAX_FREQ: int = 4000


def read_input() -> tuple[list[int]]:
    """Read input data."""
    tones: list[int] = list(map(int, INPUT[0].split()))
    verdicts = [0]
    for num in map(int, INPUT[1].split()):
        verdicts.append(num)
    return tones, verdicts


def find_freq(tones: list[int], verdicts: list[int]) -> tuple[int]:
    """Find frequency limits."""
    min_freq: int = MIN_FREQ
    max_freq: int = MAX_FREQ
    for i in range(1, len(tones)):
        avg: float = (tones[i] + tones[i - 1]) / 2
        if verdicts[i] == 1:
            if tones[i] > tones[i - 1] and min_freq < avg:
                min_freq = avg
            elif tones[i] < tones[i - 1] and max_freq > avg:
                max_freq = avg
        else:
            if tones[i] > tones[i - 1] and max_freq > avg:
                max_freq = avg
            elif tones[i] < tones[i - 1] and min_freq < avg:
                min_freq = avg
    return int(min_freq), int(max_freq)


def main():
    tones, verdicts = read_input()
    print(*find_freq(tones=tones, verdicts=verdicts))


if __name__ == '__main__':
    main()
