sample_input1 = "X..........................X.......X..........X......................X..X..........................X"
sample_input2 = "...................................................................................................."
sample_input3 = "............................................X......................................................."
sample_input4 = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
def target_practice(map: str):

    smaller_strings = [map[i:i+10] for i in range(0, len(map), 10)]

    x_coordinates = []
    i = 9
    for row_number, row in enumerate(smaller_strings):
        x_indices = [index for index, char in enumerate(row) if char == 'X']
        if x_indices:
            x_coordinates.extend([(x, i) for x in x_indices])
        i -= 1

    one_point = [(0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(9,8),(9,7),(9,6),(9,5),(9,4),(9,3),(9,2),(9,1),(9,0),(8,0),(7,0),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8)]
    two_points = [(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(8,7),(8,6),(8,5),(8,4),(8,3),(8,2),(8,1),(7,1),(6,1),(5,1),(4,1),(3,1),(2,1),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
    three_points = [(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(7,6),(7,5),(7,4),(7,3),(7,2),(6,2),(5,2),(4,2),(3,2),(2,2),(2,3),(2,4),(2,5),(2,6)]
    four_points = [(3,6),(4,6),(5,6),(6,6),(6,5),(6,4),(6,3),(5,3),(4,3),(3,3),(3,4),(3,5)]
    five_points = [(4,5),(5,5),(4,4),(5,4)]
    scored_points = 0
    
    for coordinate in x_coordinates:
        if coordinate in one_point:
            scored_points += 1
        elif coordinate in two_points:
            scored_points += 2
        elif coordinate in three_points:
            scored_points += 3
        elif coordinate in four_points:
            scored_points += 4
        elif coordinate in five_points:
            scored_points += 5

    return scored_points

if __name__ == "__main__":
    print(target_practice(sample_input1))
    print(target_practice(sample_input2))
    print(target_practice(sample_input3))
    print(target_practice(sample_input4))

