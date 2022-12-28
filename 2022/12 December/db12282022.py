"""
Given a string s, reverse all of its characters that are letters and return the resulting string.

Ex: Given the following string s…

s = "abc*a", return "acb*a".
Ex: Given the following string s…

s = "Ab&e]a-Ta", return "aT&a]e-bA".
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.reverseOnlyLetters("abc*a") == "acb*a"
    assert solution.reverseOnlyLetters("Ab&e]a-Ta") == "aT&a]e-bA"
