"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

Zadanie -- mamy dostępny zbiór sylab, oraz pewne słowo `word`; pytanie -- czy przy użyciu tych sylab
(każdą można użyć dowolną liczbę razy, również 0) można utworzyć dane słowo.

"""


def construct_word(syllables: set[str], word: str) -> bool:
    sylables_to_check = [word[i:i+2] for i in range(len(word) - 1)]
    
    for sylable in sylables_to_check:
        if sylable not in syllables:
            return False
    return True