"""
Given two strings, s and t, merge the two strings together alternating characters starting with s.
Note: If one string is longer than the other, append the remaining characters of the longer string
at the end of the merged string.


s = "abc", t = "def", return "adbecf".
"""


class Solution:
    def solve(self, s, t):
        # Write your code here
        if len(s) > len(t):
            s, t = t, s
        res = []
        for i, v in enumerate(s):
            res.extend((v, t[i]))
        res.extend(t[len(s) :])
        return "".join(res)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.solve("abc", "def"))  # "adbecf"
