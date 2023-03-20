from decorators import time_measure_decorator

@time_measure_decorator
def main():
    a = 0
    # while a < 1:
    while a < 1_000_000:


        result = None


        a += 1
    print(result)

@time_measure_decorator
def main_2():
    a = 0
    # while a < 1:
    while a < 1_000_000:


        result = None

    
        a += 1
    print(result)

if __name__ == '__main__':
    main()
    main_2()





""""

ДЛЯ ТЕСТА ДЕКОРАТОРА ПАМЯТИ!!!

"""
# INPUT = [
#     [1, 1, 1, 1],
#     [9, 9, 9, 9],
#     [2, 4, 2, 7],
#     [9, 9, 9, 9]
# ]

# @time_measure_decorator
# def dict_true(input):
#     a = 1
#     while a < 10000000:
#         di = {
#             1: 0,
#             2: 0,
#             3: 0,
#             4: 0,
#             5: 0,
#             6: 0,
#             7: 0,
#             8: 0,
#             9: 0}
#         for row in input:
#             for _ in row:
#                 di[_] += 1
#         a += 1
#     print(di)

# @time_measure_decorator
# def dict_false(input):
#     a = 1
#     while a < 10000000:
#         di = {}
#         for row in input:
#             for _ in row:
#                 if _ not in di:
#                     di[_] = 0
#                 di[_] += 1
#         a += 1
#     print(di)

# dict_true(INPUT)
# dict_false(INPUT)