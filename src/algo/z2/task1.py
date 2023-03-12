from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    seed(111)
    return [randint(0, 10 ** 6) for _ in range(data_size)]



def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 1000:
        print(f'testing solver for {size=}')
        data1,data2 = generator(size),generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data1,data2)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10**6)
        size *= 2

    return sizes, times