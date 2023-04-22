def b(lista):
    return list(set([elem for elem in lista if lista.count(elem) > 1])) if len(lista) != len(set(lista)) else True
