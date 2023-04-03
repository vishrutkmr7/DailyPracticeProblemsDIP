"""
Given an array of words, return all strings in words that are a substring of another word.
Note: The order in which you return the substrings does not matter.

Ex: Given the following words…

words = ["abc", "a", "b"], return ["a", "b"].
Ex: Given the following words…

words = ["ab", "ba", "c"], return [].
"""

import itertools


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        substrings = {
            words[i]
            for i, j in itertools.product(range(len(words)), range(len(words)))
            if i != j and words[i] in words[j]
        }
        return list(substrings)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.stringMatching(["abc", "a", "b"]))
    print(solution.stringMatching(["ab", "ba", "c"]))
