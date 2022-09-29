"""
Given a string, s, return the length of the last word.
Note: You may not use any sort of split() method.

Ex: Given the following string…

s = "The Daily Byte", return 4 (because "Byte" is four characters long).
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("The Daily Byte"))
