#  This problem was recently asked by LinkedIn:

# Write a function that reverses the digits a 32-bit signed integer, x.
# Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1].
# The function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        # Fill this in.
        negFlag = False
        if x < 0:
            negFlag = True
            x = -x

        prev_rev = 0
        rev = 0
        while x != 0:
            curr = x % 10
            rev = (rev * 10) + curr
            if rev >= 2147483647 or rev <= -2147483648:
                rev = 0
            if (rev - curr) // 10 != prev_rev:
                return 0

            prev_rev = rev
            x = x // 10  # Returns quotient floor value

        return -rev if negFlag else rev


print(Solution().reverse(123))
# 321
print(Solution().reverse(2 ** 31))
# 0
