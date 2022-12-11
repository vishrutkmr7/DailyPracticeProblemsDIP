"""
Given an string, num that represents the string form of an integer, return whether or not the
number looks the same when turned upside-down.

Ex: Given the following num...

num = “0”, return true.
Ex: Given the following num...

num = “96”, return true.
Ex: Given the following num...

num = “003821”, return false.
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        return all(d.get(n) == num[~i] for i, n in enumerate(num))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isStrobogrammatic("0") is True
    assert solution.isStrobogrammatic("96") is True
    assert solution.isStrobogrammatic("003821") is False
    print("All tests passed.")
