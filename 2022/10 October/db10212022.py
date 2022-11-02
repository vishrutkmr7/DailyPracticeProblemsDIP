"""
Given a string s and a string code, return whether or not s could have been encrypted using the pattern represented in code.

Ex: Given the following s and code...

s = “the daily byte”, code = “abc”, return true
Ex: Given the following s and code...

s = “the daily byte curriculum”, code = “abcc”, return false because ‘c’ in code already maps to the word “byte”
"""


class Solution:
    def isEncrypted(self, s: str, code: str) -> bool:
        s = s.split()
        if len(s) != len(code):
            return False
        d = {}
        for i, j in enumerate(code):
            if j not in d:
                d[j] = s[i]
            elif d[j] != s[i]:
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isEncrypted("the daily byte", "abc"))
    print(solution.isEncrypted("the daily byte curriculum", "abcc"))
