from gen_train_data import generate_data

def is_connected_with_stopover(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    destinations = [x for x in train_data if x[0] == a]
    
    for train in destinations:
        for t in train_data:
            if t[1] == b and t[0] != train[0] and train[1] == t[0]:
                return True
    return False

if __name__ == "__main__":
    train_data = generate_data(20)
    print(is_connected_with_stopover(train_data,1,3))
