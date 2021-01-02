from functools import lru_cache


class Solution:
    @lru_cache
    def minDistance(self, a: str, b: str) -> int:
        if len(a) == 0:
            return len(b)
        elif len(b) == 0:
            return len(a)
        elif a[0] == b[0]:
            return self.minDistance(a[1:], b[1:])
        else:
            return 1 + min(
                self.minDistance(a[1:], b),
                self.minDistance(a, b[1:]),
                self.minDistance(a[1:], b[1:]),
            )


s = Solution()
assert s.minDistance("horse", "ros") == 3
assert s.minDistance("intention", "execution") == 5
