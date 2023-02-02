"""
Given a binary array, bits, return the maximum number of contiguous ones within
the array.

Ex: Given the following bits…

bits = [1, 0, 1, 1], return 2.
Ex: Given the following bits…

bits = [0, 0, 0], return 0.
"""


class Solution:
    def findMaxConsecutiveOnes(self, bits: list[int]) -> int:
        count = 0
        max_count = 0
        for bit in bits:
            if bit == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)


# Test Cases
if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1]))
    print(Solution().findMaxConsecutiveOnes([0, 0, 0]))
