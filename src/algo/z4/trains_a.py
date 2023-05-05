from gen_train_data import generate_data

def get_city_most_connections(train_data: list[tuple[int,int]])->int:
    counter = {}
    for train in train_data:
        if train[0] not in counter:
            counter[train[0]] = 1
        else:
            counter[train[0]] += 1 
    max_pair = max(counter.items(), key=lambda x: x[1])
    return max_pair[0]

if __name__ == "__main__":
    train_data = generate_data(20)
    print(get_city_most_connections(train_data))
