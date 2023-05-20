
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""


def split_to_syllables(word: str) -> list[str]:
    sylaby = []
    for i in range(len(word) - 1):
        sylaba = word[i:i+2]
        sylaby.append(sylaba)
    return sylaby
