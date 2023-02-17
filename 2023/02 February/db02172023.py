"""
Given a binary string, binary, return the maximum score of the string. The score of a string is given by
splitting the string at a specific index and summing the total number of zeroes in the left substring and
the total number of ones in the right substring.
Note: Both the left and right substring after the split must have at least a single character.

Ex: Given the following string binary…

binary = "10", return 0.
Ex: Given the following string binary…

binary = "0011", return 4.
"""


class Solution:
    def maxScore(self, binary: str) -> int:
        start, end = 0, len(binary)
        left = right = ""
        for i in range(1, end):
            left, right = binary[:i], binary[i:]
            count_0 = left.count("0")
            count_1 = right.count("1")
            start = max(start, count_0 + count_1)
        return start


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScore("10"))
    print(solution.maxScore("0011"))
