"""
Given an array of integers, nums, sorted in ascending order, return the element that occurs more than one fourth of the time.
Note: If no element appears more than a fourth of the time, return -1.

Ex: Given the following nums…

nums = [1, 2, 2, 3, 4], return 2.
Ex: Given the following nums…

nums = [1, 2, 3, 4], return -1.
"""


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        try:

            def findIndexOfFirst(x):
                l = 0
                r = len(arr) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if arr[mid] < x:
                        l = mid + 1
                    else:
                        r = mid - 1
                return l

            for q in range(1, 4):
                idx = int(q * len(arr) / 4)
                start = findIndexOfFirst(arr[idx])
                if arr[start] == arr[start + len(arr) // 4]:
                    return arr[start]
        except Exception:
            return -1

    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findSpecialInteger([1, 2, 2, 3, 4]))
    print(solution.findSpecialInteger([1, 2, 3, 4]))
