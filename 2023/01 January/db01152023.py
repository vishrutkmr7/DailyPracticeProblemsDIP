"""
You are given an integer, n, and a binary number represented as an integer array, binary. Each of the
one bits in binary must be separated by at least one zero bit otherwise the bits become angry.
Return whether or not it’s possible to flip at least n zero bits to one bits without making the
bits angry.

Ex: Given the following binary and n…

binary = [1, 0, 0, 1], n = 1, return false.
Ex: Given the following binary and n…

binary = [0, 1, 0, 0, 1, 0, 0, 0, 1], n = 1, return true.
"""


class Solution:
    def angryBits(self, binary: list[int], n: int) -> bool:
        if n == 0:
            return True

        count = 0
        for i, v in enumerate(binary):
            if v == 0:
                if i == 0:
                    if binary[i + 1] == 0:
                        count += 1
                elif i == len(binary) - 1:
                    if binary[i - 1] == 0:
                        count += 1
                elif binary[i - 1] == 0 and binary[i + 1] == 0:
                    count += 1
        return count >= n


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.angryBits([1, 0, 0, 1], 1))
    print(solution.angryBits([0, 1, 0, 0, 1, 0, 0, 0, 1], 1))
