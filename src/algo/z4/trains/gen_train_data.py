"""
System "pocigągów" ... de facto połączeń między miastami reprezentowanymi przez liczby

[(4,8), (1,3), (2,2), (3, 1), (1,10)]


"""
from random import randint, seed

N_CITIES = 20
seed(111)


def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res


if __name__ == '__main__':
    train_schedule = generate_data(40)
    destinations = [[] for _ in range(N_CITIES)]
    for (src, dst) in train_schedule:
        # .... jakoś trzeba zupdate'ować do destinations[src]
        pass

    # jakoś trzeba przejść przez destinations i sprawdzić który src ma najdłuższą listę destinations[src]
