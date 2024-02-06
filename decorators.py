import time


def time_measure_decorator(func):
    """Декоратор измерения времени выполнения функции."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {func.__name__}: {end - start} сек.')
        return result
    return wrapper


if __name__ == '__main__':
    """Пример для пояснения алгоритма работы декораторов."""

    def decorator_function(func):
        def wrapper(*args, **kwargs):
            print('Выполняем обёрнутую функцию.')
            func(*args, **kwargs)
            print('Выходим из обёртки.')
        return wrapper

    @decorator_function
    def hello_world(a, b):
        print('Зашли в функцию.')
        print(f'Значение a составляет: {a}.')
        print(f'Значение b составляет: {b}.')
        print('Выходим из функции.')
        return

    hello_world(a=100, b=2)
