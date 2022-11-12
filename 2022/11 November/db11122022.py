"""
Given a sorted integer array nums and a target, search for the target with in the array.
If the targets exists within the array, return its index. If it does not exist within the array,
return -1. 

Ex: Given the following nums and target...

nums = [-5, -3, 0, 3, 8, 12, 40], target = 8, return 4.
Ex: Given the following nums and target...

nums = [1, 2, 3, 6, 8], target = 10, return -1.
"""


def binary_search(nums, target):
    """Searches for target within nums"""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return binary_search(nums, target)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-5, -3, 0, 3, 8, 12, 40], 8))
    print(solution.search([1, 2, 3, 6, 8], 10))
