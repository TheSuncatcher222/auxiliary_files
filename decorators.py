import time

"""Декоратор измерения времени выполнения функции."""
def time_measure_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {func.__name__}: {end - start} сек.')
        return result
    return wrapper
