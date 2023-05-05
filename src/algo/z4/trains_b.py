"""
zadanie2:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" (bez przesiadek).
"""
from gen_train_data import generate_data

def is_connected(train_data: list[tuple[int,int]], city_a:int,city_b:int)->bool:
    for train in train_data:
        if train[0] == city_a and train[1] == city_b:
            return True
    return False

if __name__ == "__main__":
    train_data = generate_data(20)
    print(is_connected(train_data,1,3))
