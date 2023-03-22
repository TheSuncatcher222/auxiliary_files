"""
Для заданных коэффициентов уравнения вида ax^2 + bx + c = 0 найти его корни.
Гарантируется, что входными данными будут три целочисленных числа, указанные
через пробел. Ответ необходимо вывести строкой, указав числа через пробел
в порядке их возрастания.
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: str = '0 0 0'  # Бесконечное множество решений
INPUT_2: str = '0 0 5'  # Нет решений
INPUT_3: str = '0 5 5'  # Один корень: -1.0
INPUT_4: str = '2 1 4'  # Нет решений
INPUT_5: str = '2 4 2'  # Один корень: -1.0
INPUT_6: str = '2 5 2'  # Два корня: -0.5 и -2.0

INPUT: str = INPUT_1


def read_input() -> tuple:
    """Read input data."""
    nums: list = INPUT.split()
    a: int = int(nums[0])
    b: int = int(nums[1])
    c: int = int(nums[2])
    return a, b, c


def solve_square(a: int, b: int, c: int) -> tuple or int or None:
    """Solve square equation."""
    disc: int = b * b - 4 * a * c
    if disc < 0:
        return None
    # Optimize formula: (-b + disc ** 0.5) / (2 * a)
    disc_sqrt = disc ** 0.5
    disc_const = -b / (2 * a)
    x1 = disc_const + disc_sqrt / (2 * a)
    if disc == 0:
        return x1
    x2 = disc_const - disc_sqrt / (2 * a)
    return x1, x2


def solve_equation(a, b, c) -> str or int or tuple:
    """Solve given equation."""
    if a == 0:
        if c == 0:
            return '∞'
        elif b == 0:
            return f'Error! Given equation is: {c} = 0'
        return - b / c
    return solve_square(a, b, c)


def reformat_answer(answer: any) -> str or None:
    """Reformat answer to desire string."""
    if answer is None or isinstance(answer, str):
        return answer
    elif isinstance(answer, tuple):
        return ' '.join(map(str, sorted(answer)))
    elif isinstance(answer, float):
        return str(answer)


def main():
    a, b, c = read_input()
    answer: any = solve_equation(a=a, b=b, c=c)
    print(reformat_answer(answer=answer))


if __name__ == '__main__':
    main()
