error = -1


def longest_sequence(s: str, symbol: str)->int:
    if len(s) == 0: return 0

    unwanted_char_check = ''.join([x for x in s if x in ["<",">"]]) #just to make sure there is nothing else than "<" and ">"
    if len(unwanted_char_check) != len(s): return error
    
    if symbol in ["<",">"]:
        if symbol == ">":
            return max([len(x) for x in s.split("<")])
        
        elif symbol == "<":
            return max([len(x) for x in s.split(">")])
    else: return error
