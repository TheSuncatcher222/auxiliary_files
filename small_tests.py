from decorators import time_measure_decorator

@time_measure_decorator
def main():
    a = 0
    # while a < 1:
    while a < 1_000_000:


        result = None


        a += 1
    # print(result)

@time_measure_decorator
def main_2():
    a = 0
    # while a < 1:
    while a < 1_000_000:


        result = None

    
        a += 1
    # print(result)

if __name__ == '__main__':
    main()
    main_2()