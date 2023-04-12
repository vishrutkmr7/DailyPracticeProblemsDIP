"""
Given two strings, s and t, return whether or not its possible to transform s into t by doing
any number of conversions. A single conversion consists of converting all occurrences of
one character in s into any other lowercase alphabetical character.
Note: Both s and t will only contain lowercase alphabetical characters and will always contain
the same number of characters.

Ex: Given the following s and t…

s = "abc", t = "bbc", return true (convert all "a" characters to "b" characters).
Ex: Given the following s and t…

s = "bbd", t = "cde", return false.
"""


class Solution:
    def canConvert(self, s: str, t: str) -> bool:
        if s == t:
            return True
        dp = {}
        return next(
            (False for i, j in zip(s, t) if dp.setdefault(i, j) != j),
            len(set(t)) < 26,
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.canConvert("abc", "bbc"))
    print(solution.canConvert("bbd", "cde"))
