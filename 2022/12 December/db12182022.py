"""
Given a string S that contains only lowercase letters, return a list containing the intervals of all
the bunches. A bunch is a set of contiguous characters (larger than two) that are all the same.
An interval that represents a bunch contains the starting index of the bunch and the ending index of
the bunch.
Note: The intervals returned should be in ascending order according to start indexes. 
Ex: Given the following string S...

S = “aaabbbccc”, return [[0,2],[3,5],[6,8]].
Ex: Given the following string S...

S = “aaabbcddddd”, return [[0,2],[6,10]].
"""


class Solution:
    def bunches(self, s: str) -> list[list[int]]:
        bunches = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if i - start > 2:
                    bunches.append([start, i - 1])
                start = i
        if len(s) - start > 2:
            bunches.append([start, len(s) - 1])
        return bunches


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.bunches("aaabbbccc"))
    print(solution.bunches("aaabbcddddd"))
