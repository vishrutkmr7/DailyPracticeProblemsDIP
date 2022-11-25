"""
Given an array of integers, nums, and a value k, return the number of continuous sub-arrays
that sum to k.

Ex: Given the following nums and k…

nums = [1,1,4], k = 5, return 1.
Ex: Given the following nums and k…

nums = [3, 2, 2, 1, 1, 1], k = 5, return 3.
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # O(n) time | O(n) space
        count = 0
        prefix_sum = {0: 1}
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                count += prefix_sum[current_sum - k]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 4], 5))
    print(solution.subarraySum([3, 2, 2, 1, 1, 1], 5))
