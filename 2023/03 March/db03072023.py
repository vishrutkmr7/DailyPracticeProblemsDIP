"""
Given two string arrays, word1 and word2, return whether or not the two arrays represent the same string.

Ex: Given the following word1 and word2…

word1 = ["abc", "d"], word2 = ["ab", "cd"], return true.
Ex: Given the following word1 and word2…

word1 = ["a", "b", "c"], word2 = ["a", "b", "d"], return false.
"""


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.arrayStringsAreEqual(["abc", "d"], ["ab", "cd"]))
    print(solution.arrayStringsAreEqual(["a", "b", "c"], ["a", "b", "d"]))
