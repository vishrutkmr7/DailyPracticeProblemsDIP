"""
Given a string permitted and a string array, words, valid words are strings within words
that only contain permitted characters. Return the total number of valid words.

Ex: Given the following permitted and words…

permitted = "abc", words = ["d", "ab", "abce"], return 1.
Ex: Given the following permitted and words…

permitted = "ake", words = ["ail", "kea", "a"], return 2.
"""


class Solution:
    def countValidWords(self, permitted: str, words: list[str]) -> int:
        return sum(all((char in permitted for char in word)) for word in words)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countValidWords("abc", ["d", "ab", "abce"]))
    print(solution.countValidWords("ake", ["ail", "kea", "a"]))
