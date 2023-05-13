from gen_train_data import generate_data

def print_destinations(destinations: list[list[int]]):
    for i, dest in enumerate(destinations):
        print(i, '->', dest)


def extract_destination_info(train_data: list[tuple[int, int]]):
    """
    Turns a list of [from,to] tuples into an info of the sort
    city -> list of destinations reachable from the city

    :param train_data:
    :return:
    """
    max_city = max([start for start, end in train_data])
    destinations = [[] for _ in range(max_city + 1)]
    for start, end in train_data:
        destinations[start].append(end)
    return destinations

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
