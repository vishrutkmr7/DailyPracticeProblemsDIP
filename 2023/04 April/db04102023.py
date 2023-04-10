"""
Given a binary array (i.e. an array containing only zeroes and ones), bits,
return the length of the longest streak of ones after deleting one element from the given bits.

Ex: Given the following bits…

bits = [0, 1, 1, 0, 1], return 3.
Ex: Given the following bits…

bits = [1, 1, 1, 1, 1], return 4.
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if sum(nums) == n:
            return n - 1

        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = nums[0]

        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0], dp[i][1] = dp[i - 1][0] + 1, dp[i - 1][1] + 1
            else:
                dp[i][0], dp[i][1] = 0, dp[i - 1][0]

        return max(i for j in dp for i in j)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.longestSubarray([0, 1, 1, 0, 1]) == 3
    assert solution.longestSubarray([1, 1, 1, 1, 1]) == 4
    assert solution.longestSubarray([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]) == 7
    assert solution.longestSubarray([0, 0, 0, 1]) == 1
    print("All test cases passed!")
