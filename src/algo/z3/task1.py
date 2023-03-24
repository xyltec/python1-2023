from random import seed, randint

def run_tests(generator, solver, step_factor=1.3, max_size=10 ** 5):
    size = 10
    sizes = []
    times = []
    while size < max_size:
        print(f'testing solver for {size=:.0f} ...', end=' ')
        data = generator(int(size))
        REPETITIONS = 0
        time_sum = 0
        while True:
            st = datetime.now().timestamp()
            ret = solver(**data)
            en = datetime.now().timestamp()
            time_sum += (en - st)
            REPETITIONS += 1
            if time_sum > 0.1:
                break

        sizes.append(size)
        exec_time = time_sum / REPETITIONS * 10 ** 6
        print(f' execution time: {int(exec_time / 10**3)}ms')
        times.append(exec_time)
        size *= step_factor

    return sizes, times


def solve(a: list[int]) -> int:
    max_result = 0
    for i in range(len(a)-1):
        res = a[i] * a[i+1]
        if res > max_result:
            max_result = res
    return max_result

def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
