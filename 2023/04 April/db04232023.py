"""
Given two integers, N and start, return the result of applying the XOR operation to N
values beginning from start.
Note: Each value that is calculated should be formed as follows: start + 2 * i
(where i is the ith value you're calculating).

Ex: Given the following N and start…

N = 3, start = 0, return 6 (0 ^ 2 ^ 4 = 6).
Ex: Given the following N and start…

N = 5, start = 3, return 3.
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.xorOperation(3, 0))
    print(solution.xorOperation(5, 3))
