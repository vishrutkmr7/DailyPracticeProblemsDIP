"""
This question is asked by Apple.
Given a string and a character, return an array of integers where each index is the shortest distance from the character.
Ex: Given the following string s and character s...

s = "dailybyte", c = 'y', return [4, 3, 2, 1, 0, 1, 0, 1, 2]
"""


class Solution:
    def shortestDistance(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [n] * n
        prev = -n
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], i - prev)
        prev = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.shortestDistance("dailybyte", "y") == [4, 3, 2, 1, 0, 1, 0, 1, 2]
    assert solution.shortestDistance("dailybyte", "d") == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("All tests passed.")
