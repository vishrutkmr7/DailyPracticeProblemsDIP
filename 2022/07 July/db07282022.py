"""
You are transporting bricks on a construction site and want to work as efficiently as possible.
The weight of each brick is given by bricks[i]. Given a wheelbarrow that can carry up to (not including) 5000 pounds,
return then maximum number of bricks you can place in your wheelbarrow to transport.

Ex: Given the following bricks…

bricks = [1000, 1000, 1000, 2000], return 3.

Ex: Given the following bricks…

bricks = [1000, 200, 150, 200], return 4.
"""


class Solution:
    def maxBricks(self, bricks: list[int], limit: int) -> int:
        # sort the bricks by weight
        bricks.sort()
        if sum(bricks) < limit:
            return len(bricks)
        else:
            return self.maxBricks(bricks[1:], limit)


# Test Cases
print(Solution().maxBricks([1000, 1000, 1000, 2000], 5000))
print(Solution().maxBricks([1000, 200, 150, 200], 5000))
