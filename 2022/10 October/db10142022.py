"""
Given an image represented as a 2D array of pixels, return the image rotation ninety degrees.

Ex: Given the following image…

image = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
], return the image such that it's been modified as follows...
[
    [16,13,10],
    [17,14,11],
    [18,15,12]
]
"""


class Solution:
    def rotateImage(self, image: list[list[int]]) -> list[list[int]]:
        return [list(row) for row in zip(*image[::-1])]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.rotateImage([[10, 11, 12], [13, 14, 15], [16, 17, 18]]) == [
        [16, 13, 10],
        [17, 14, 11],
        [18, 15, 12],
    ]
    print("All tests passed.")
