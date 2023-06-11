import string
import random
def encoder(s: str) ->str:
    alphabet = [x for x in string.ascii_lowercase]
    letters = [x for x in s]
    res = ""
    for letter in letters:
        res += letter
        for i in range(random.randint(1,4),random.randint(5,7)):
            random_letter = alphabet[random.randint(0,len(alphabet) - 1)]
            res += random_letter
    random_value = random.randint(1,10)
    decrypt_key = ([(res.find(w)+random_value) for w in s], random_value)

    return res,decrypt_key


def decoder(s: str, decrypt_key: list[int]) -> str:
    return ''.join([s[i-decrypt_key[1]] for i in decrypt_key[0]])
    


if __name__ == "__main__":
    result,key = encoder("Some example message")
    print(f"Encrypted: {result}")
    print(f"Decrypted:", decoder(result, key))
