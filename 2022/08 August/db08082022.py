"""
This question is asked by Facebook.
Given an array of unsorted integers, return the length of its longest increasing subsequence.
Note: You may assume the array will only contain positive numbers.

Ex: Given the following array nums…

nums = [1, 9, 7, 4, 7, 13], return 4.
The longest increasing subsequence is 1, 4, 7, 13.
"""


from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def LIS2(self, nums: list[int]) -> int:
        arr = [nums.pop(0)]
        for n in nums:
            if n > arr[-1]:
                arr.append(n)
            else:
                arr[bisect_left(arr, n)] = n

        return len(arr)


# Test Cases
nums = [1, 9, 7, 4, 7, 13]
print(Solution().LIS2(nums))
