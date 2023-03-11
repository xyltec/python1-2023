from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    seed(111)
    return [randint(0, 10 ** 6) for _ in range(data_size)]


def solve_problem(data):
    ret = sorted(data)
    return ret


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 100000:
        print(f'testing solver for {size=}')
        data = generator(int(size))
        REPETITIONS = 0
        time_sum = 0
        while True:
            st = datetime.now().timestamp()
            ret = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)
            REPETITIONS += 1
            if time_sum > 0.1:
                break

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 1.1

    return sizes, times


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)
    linxx = [0.01 * x_**1 for x_ in x]
    quadx = [0.01 * x_**2 for x_ in x]
    cubex = [0.01 * x_**3 for x_ in x]

    plt.plot(x, linxx, linestyle='dotted')
    plt.plot(x, quadx, linestyle='dotted')
    plt.plot(x, cubex, linestyle='dotted')
    plt.plot(x, y)
    plt.legend(['O(N)', 'O(N**2)', 'O(N**3)', 'algorytm'], loc='upper left')

    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
    plt.savefig('aa.png')
