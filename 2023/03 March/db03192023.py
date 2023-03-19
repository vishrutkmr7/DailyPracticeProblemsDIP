"""
Given an integer N, return any array that contains N elements who sum to zero.

Ex: Given the following N...

N = 1, return [0] (1 number that sums to zero is 0 itself).
Ex: Given the following N...

N = 2, return [-1, 1] (this is one possible solution).
"""


class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []
        for i in range(1, n // 2 + 1):
            result.extend((i, -i))
        if n % 2 == 1:
            result.append(0)
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumZero(1))
    print(solution.sumZero(2))
    print(solution.sumZero(3))
    print(solution.sumZero(4))
    print(solution.sumZero(5))
