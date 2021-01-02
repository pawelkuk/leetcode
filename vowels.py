from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        return sum(self.solve(n - 1, c) for c in ["a", "e", "i", "o", "u"]) % (
            10 ** 9 + 7
        )

    @lru_cache
    def solve(self, length: int, last_vowel: str):
        if length == 0:
            return 1
        if last_vowel == "e":
            return sum(self.solve(length - 1, c) for c in ["a", "i"])
        if last_vowel == "a":
            return sum(self.solve(length - 1, c) for c in ["e", "i", "u"])
        if last_vowel == "i":
            return sum(self.solve(length - 1, c) for c in ["e", "o"])
        if last_vowel == "u":
            return sum(self.solve(length - 1, c) for c in ["o", "i"])
        if last_vowel == "o":
            return self.solve(length - 1, "i")


s = Solution()

assert s.countVowelPermutation(1) == 5
assert s.countVowelPermutation(2) == 10
assert s.countVowelPermutation(5) == 68
print(s.countVowelPermutation(100))