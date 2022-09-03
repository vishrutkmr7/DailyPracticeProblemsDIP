"""
This question is asked by Amazon.
Given an array of integers, nums, sort the array in any manner such that when i is even,
nums[i] is even and when i is odd, nums[i] is odd.
Note: It is guaranteed that a valid sorting of nums exists.

Ex: Given the following array nums…

nums = [1, 2, 3, 4], one possible way to sort the array is [2,1,4,3]
"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = [num for num in nums if num % 2 == 0]
        odd = [num for num in nums if num % 2 != 0]
        even.sort()
        odd.sort()
        return [even.pop(0) if i % 2 == 0 else odd.pop(0) for i in range(len(nums))]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([1, 2, 3, 4]))
