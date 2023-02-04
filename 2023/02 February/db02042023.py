"""
Given a string, s, return the length of the longest substring between two characters that
are equal.
Note: s will only contain lowercase alphabetical characters. 

Ex: Given the following string s…

s = "bbccb", return 3 ("bcc" is length 3).
Ex: Given the following string s…

s = "abb", return 0.
"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        maxer = -1
        for i, val in enumerate(s):
            if val in dic:
                diff = i - dic[val] - 1
                maxer = max(maxer, diff)
            else:
                dic[val] = i
        return maxer


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxLengthBetweenEqualCharacters("bbccb"))
    print(solution.maxLengthBetweenEqualCharacters("abb"))
