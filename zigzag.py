from collections import defaultdict


def zigzag(n: int):
    if n > 1:
        i = 0
        sign = +1
        while True:
            if 0 <= i < n:
                yield i
            else:
                sign *= -1
                i += sign
            i += sign
    else:
        if n == 1:
            while True:
                yield 1


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = defaultdict(list)
        for letter, i in zip(s, zigzag(numRows)):
            d[i].append(letter)

        return "".join(["".join(x) for x in d.values()])
