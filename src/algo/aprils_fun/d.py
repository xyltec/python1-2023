"""
Funkcja sprawdzająca czy jedno imię jest przypisane do więcej niż jednego id, oraz czy do jednego id przypisane jest więcej niż jedno imię.
"""
def d(people : list[tuple[int,str]]):
    ids = {}
    names = {}
    powtorzenia_names = []
    powtorzenia_id = []
    res_id = []
    res_names = []
    for person in people:
        if person[0] not in ids.keys():
            ids[person[0]] = []
            ids[person[0]].append(person[1])
        else:
            ids[person[0]].append(person[1])

        if person[1] not in names:
            names[person[1]] = []
            names[person[1]].append(person[0])
        else:
            names[person[1]].append(person[0])
    for key,value in ids.items():
        if len(set(value)) > 1:
            if (key,value) not in powtorzenia_id:
                powtorzenia_id.append((key,len(set(value))))
    for key,value in names.items():
        if len(set(value)) > 1:
            if (key,value) not in powtorzenia_names:
                powtorzenia_names.append((key,len(set(value))))
    if len(powtorzenia_names) > 0 and len(powtorzenia_id) > 0:
        for i in range(len(powtorzenia_names)):
            res_names.append(f"dla name='{powtorzenia_names[i][0]}' pojawiają się {powtorzenia_names[i][1]} różne id's")
        for i in range(len(powtorzenia_id)):
            res_id.append(f"dla id={powtorzenia_id[i][0]} pojawiają się {powtorzenia_id[i][1]} różne names")
        return '\n'.join(res_names+res_id)
    elif len(powtorzenia_names) > 0:
        for i in range(len(powtorzenia_names)):
            res_names.append(f"dla name='{powtorzenia_names[i][0]}' pojawiają się {powtorzenia_names[i][1]} różne id's")
            return '\n'.join(res_names)
    elif len(powtorzenia_id) > 0:
        for i in range(len(powtorzenia_id)):
            res_id.append(f"dla id={powtorzenia_id[i][0]} pojawiają się {powtorzenia_id[i][1]} różne names")
        return '\n'.join(res_id)
    else:
        return 'dla każdego id przypisany jest unikalny name'
if __name__ == "__main__":
    print(d([(1,'Adam'), (2,'Jane'), (3, 'Xiao'), (4,'Jane'),(5,'Mark'),(5,'Arthur'),(7,'Jane'),(10,'Jane'),(11,'John'),(12,'John')]))
