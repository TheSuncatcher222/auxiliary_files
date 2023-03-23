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

"""Примеры с ответами для тестов."""
INPUT_1: list = [
    '1',
    '5',
    '2',
    '4 5']  # 0 1
INPUT_2: list = [
    '7',
    '100 1 50 50 100 50 0',
    '3',
    '300 0 75']  # 4 1 3

INPUT: list = INPUT_2


def read_input() -> tuple:
    """Read input data."""
    cards_quantity: int = int(INPUT[0])
    cards: list = list(map(int, INPUT[1].split()))
    peoples_quantity: int = int(INPUT[2])
    cards_required: list = list(map(int, INPUT[3].split()))
    return cards_quantity, cards, peoples_quantity, cards_required


def count_requirements(
        cards_quantity: int,
        cards: list,
        peoples_quantity: int,
        peoples_required: list[list[int, int]]) -> dict:
    """Find available cards in collection."""
    answer: dict[int, int] = {i: 0 for i in range(peoples_quantity)}
    current_people: int = 0
    cards_available: int = 0
    card_previous: int = -1
    current_card_index: int = 0
    while current_card_index < cards_quantity:
        card: int = cards[current_card_index]
        if card == card_previous:
            current_card_index += 1
        elif card <= peoples_required[current_people][1]:
            cards_available += 1
            current_card_index += 1
            card_previous = card
        else:
            answer[peoples_required[current_people][0]] = cards_available
            current_people += 1
    answer[peoples_required[current_people][0]] = cards_available
    return answer


def main():
    cards_quantity, cards, peoples_quantity, cards_required = read_input()
    cards.sort()
    peoples_required: list = []
    for i in range(peoples_quantity):
        peoples_required.append([i, cards_required[i]])
    peoples_required: list = sorted(
        peoples_required, key=lambda people: people[1])
    answer: dict[int, int] = count_requirements(
        cards_quantity, cards, peoples_quantity, peoples_required)
    print(*answer.values())


if __name__ == '__main__':
    main()
