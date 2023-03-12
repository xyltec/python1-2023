from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    seed(111)
    return [randint(0, 10 ** 6) for _ in range(data_size)]