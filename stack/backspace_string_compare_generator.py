"""String compare using generators"""
from itertools import zip_longest
def string_compare(S, T):
    def G(S):
        skip = 0
        for x in S[::-1]:
            if x == "#":
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x
    return all(x == y for x, y in zip_longest(G(S), G(T)))