"""
Given a string s, reverse the words.
Note: You may assume that there are no leading or trailing whitespaces and each word within s
is only separated by a single whitespace.

Ex: Given the following string s…

s = "The Daily Byte", return "Byte Daily The".
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("The Daily Byte"))
