"""
You are building a pool in your backyard and want to create the largest pool possible.
The largest pool is defined as the pool that holds the most water. The workers you hired to
dig the hole for your pool didn’t do a great job and because of this the depths of the pool
at different areas are not equal. Given an integer array of non-negative integers that represents
a histogram of the different heights at each position of the hole for your pool, return the largest
pool you can create.

Ex: Given the following heights...

heights = [1, 4, 4, 8, 2], return 8. 
You can build your largest pool (most water) between indices 1 and 3 (inclusive) for a water volume of 4 * 2 = 8.
"""


class Solution:
    def largestPool(self, heights: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            max_area = max(
                max_area, min(heights[left], heights[right]) * (right - left)
            )
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestPool([1, 4, 4, 8, 2]))
