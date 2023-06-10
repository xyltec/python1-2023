import string
import random

def encoder(s: str) ->str:
    alphabet = [x for x in string.ascii_lowercase]
    letters = [x for x in s]
    res = ""
    for letter in letters:
        res += letter
        for i in range(random.randint(3,5),random.randint(7,10)):
            random_letter = alphabet[random.randint(0,len(alphabet) - 1)]
            res += random_letter
    decrypt_key = []
    for w in s:
        decrypt_key.append(res.find(w))
    return res,decrypt_key


def decoder(s: str, decrypt_key: list[int]) -> str:
    decoded = ""
    for i in decrypt_key:
        decoded += s[i] 
    return decoded
    


if __name__ == "__main__":
    result,key = encoder("apple")
    print(f"Encrypted: {result}")
    print(f"Decrypted:", decoder(result, key))
