"""
Given a string, sequence, and a word to search for, return the total number of times that word can be
repeated and still exist as a substring within sequence.

Ex: Given the following sequence and word…

sequence = "abcabcab", word = "abc", return 2 ("abcabc" exists within our sequence but "abcabcabc"
does not).
Ex: Given the following sequence and word…

sequence = "ccc", word = "c", return 3.
"""


class Solution:
    def repeatedSubstringPattern(self, sequence: str, word: str) -> int:
        count = 0
        while sequence and sequence.startswith(word):
            count += 1
            sequence = sequence[len(word) :]
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedSubstringPattern("abcabcab", "abc"))
    print(solution.repeatedSubstringPattern("ccc", "c"))
