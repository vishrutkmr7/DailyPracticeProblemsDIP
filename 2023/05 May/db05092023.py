"""
Given an integer, N, return all values between one and N (inclusive) in lexicographical order.
Note: N will not exceed one million.

Ex: Given the following N…

N = 11, return [1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9].
"""


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        return sorted(list(range(1, n + 1)), key=str)

    def lexicalOrder2(self, n: int) -> list[int]:
        # O(n) time, O(1) extra space.
        ans = [1]
        for _ in range(n - 1):
            i = ans[-1]
            if 10 * i <= n:
                ans.append(10 * i)
            else:
                while i + 1 > n or (i + 1) % 10 == 0:
                    i //= 10
                ans.append(i + 1)
        return ans


# Test Cases
if __name__ == "__main__":
    print(Solution().lexicalOrder(11))
    print(Solution().lexicalOrder2(1000000))
