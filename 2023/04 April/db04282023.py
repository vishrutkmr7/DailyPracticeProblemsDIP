"""
You are given an integer array, bits, that only contains zeroes and ones and represents a binary
sequence. Within our binary, there are two characters that are represented. One character can be
represented by a single bit, 0, and another character can be represented with two bits, 10, or 11.
Return whether or not the last character in our binary sequence is the character represented by a 0.
Note: The bits will always end with a zero.

Ex: Given the following bits…

bits = [1, 0, 0], return true (our binary can be decoded as our two-bit character followed by our
one-bit character).
Ex: Given the following bits…

bits = [1, 0, 1, 0], return false.
"""


class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        res = True
        for bit in bits[-2::-1]:
            if bit:
                res = not res
            else:
                break
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isOneBitCharacter([1, 0, 0]))  # True
    print(solution.isOneBitCharacter([1, 0, 1, 0]))  # False
