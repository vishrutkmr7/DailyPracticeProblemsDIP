"""
You are given a dataset represented as an integer array, nums that contains values between one and n.
Inside the data set, an error has occurred such that one of the values between one and n has been
duplicated to another number between one and n. Because of this, one of the values between one and n
appears twice and one value does not appear at all. Return the missing value and the values that
appears twice.

Ex: Given the following nums…

nums = [1, 3, 2, 5, 5], return [5, 4].
Ex: Given the following nums…

nums = [1, 2, 3, 3], return [3,4].
"""


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n, total, total_og = len(nums), sum(nums), sum(set(nums))
        s = n * (n + 1) // 2
        return [total - total_og, s - total_og]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findErrorNums([1, 3, 2, 5, 5]))
    print(solution.findErrorNums([1, 2, 3, 3]))
