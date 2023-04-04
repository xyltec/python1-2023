from random import randint, seed

N_CITIES = 20
seed(111)

def generate_data(data_size):
    return [(randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)) for i in range(data_size)]

if __name__ == '__main__':
    rr = generate_data(10)
    print(rr)
