"""
Given an array digits that represents a non-negative integer, add one to the number
and return the result as an array. 

Ex: Given the following digits...

digits = [1, 2], return [1, 3].
Ex: Given the following digits...

digits = [9, 9], return [1, 0, 0].
"""


class Solution:
    def plusOne(self, digits):
        """Plus one"""
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2]))
    print(solution.plusOne([9, 9]))
