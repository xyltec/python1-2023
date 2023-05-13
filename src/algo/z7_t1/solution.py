
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek


"""




def open_lock(key: list[int], lock: list[int]) -> int:
    """
    :param key:   np. [4,1,1,3,1,2]
    :param lock:  np  [1,4,2,2,4,3]
    :return:    -1 jeśli wartości są "invalid" (np. <0); 0 jeśli klucz otwiera zamek, 1 jeśli klucz nie otwiera zamka
    """
    if len(key) == 0 or len(lock) == 0 or len(key) != len(lock):
        return -1
    else:
        required_sum = key[0] + lock[0]
        for i in range(len(key)):
            if key[i] < 0 or lock[i] < 0:
                return -1
            elif key[i] + lock[i] != required_sum:
                return 1
        return 0


if __name__ == "__main__":
    print(open_lock([4,1,1,3,1,2],[1,4,2,2,4,3]))





