M = 1000
data: list[list]


def get_new_bag(data_size: int):
    return [[] for _ in range(data_size)]


def insert_element(bag: list[list], element: int):
    h = element.__hash__()
    # todo -- wrzucić odpowiednio hash `h` do bag
    # 1) sprawdzić czy już jest w bag-u; jeśli tak to return
    # 2) jeśli nie jest, to sprawdzić indeks listy do której trzeba wrzucić element, np. `idx`, i potem wrzucić
    # ten element do bag[idx]
    #

def contains_element(bag: list[list], element: int) -> bool:
    h = element.__hash__()
    # todo: sprawdzić czy `x` z hashem `h` jest w `bag`
    # odpowiednio zawężony (do [0...M-1] hash ma być numerem listy)
    # wyliczyć "indeks listy" z hasha,
    # sprawdzić czy bag[idx] zawiera `element`


def remove_element(bag: list[list], element: int) -> bool:
    h = element.__hash__()
    # todo: usunąć `x` z hashem `h` z `bag`
    # wyliczyć "indeks listy" z hasha,
    # usunąć z listy bag[idx] element `element`



if __name__ == '__main__':
    bag = get_new_bag(1000)  # np. bag[0] jest listą... i bag[999]...
    insert_element(bag, 17)
    insert_element(bag, 17)
    insert_element(bag, 32)

    print(contains_element(bag, 17), True)
    print(contains_element(bag, 18), False)
    remove_element(bag, 32)
    print(contains_element(bag, 32), False)
    remove_element(bag, 17)
    print(contains_element(bag, 17), False)
