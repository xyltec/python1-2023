
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
    
    if len(lock)<0 or len(key)<0 or len(lock)!=len(key) or min(lock)<0 or min(key)<0:
        return -1
    war = lock[0] + key[0]
    for i in range(1,len(lock)):
        if war != lock[i]+key[i]:
            return 1
    return 0
