# This problem was recently asked by LinkedIn:

# Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer.
# The most significant digit is at the front of the array and each element in the array contains only one digit.
# Furthermore, the integer does not have leading zeros, except in the case of the number '0'.


class Solution:
    def plusOne(self, digits):
        # Fill this in.
        num = ""
        for i in range(0, len(digits)):
            num = num + str(digits[i])

        sol = int(num) + 1
        sol = list(str(sol))
        for j in range(0, len(sol)):
            sol[j] = int(sol[j])

        return sol


num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]
