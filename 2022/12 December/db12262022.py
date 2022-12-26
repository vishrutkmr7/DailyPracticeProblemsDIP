"""
Given two strings, source and target, return the minimum number of subsequences of source that can be used to form target.
Note: If it is impossible to use subsequences of source to form target, return -1.
Ex: Given the following source and target…

source = "abc", target = "def", return -1.
Ex: Given the following source and target…

source = "abcdef", target = "abcadaef", return 3.
"""


class Solution:
    def minSubsequences(self, source: str, target: str) -> int:
        # Write your code here
        def inc():
            self.cnt += 1
            return 0

        self.cnt = i = 0
        for t in target:
            i = source.find(t, i) + 1 or source.find(t, inc()) + 1
            if not i:
                return -1
        return self.cnt + 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubsequences("abc", "def"))
    print(solution.minSubsequences("abcdef", "abcadaef"))
