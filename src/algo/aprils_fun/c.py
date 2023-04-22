def c(people : list[tuple[int,str]]):
    ids = {}
    for person in people:
        if person[0] not in ids.keys():
            ids[person[0]] = 1
        else:
            ids[person[0]] += 1
    for key,value in ids.items():
        if value > 1:
            return f'dla id={key} pojawiają się {value} różne names'
    return 'dla każdego id przypisany jest unikalny name'
if __name__ == "__main__":
    print(c([(1,'Adam'), (2,'Jane'), (3, 'Xiao'), (4,'Jane'),(5,'Mark')]))
