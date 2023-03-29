"""
You are a wandering traveler following direction. You are given a string path,
each character in the string is either a N, E, S, or W representing a movement
one unit north, east, south, and west respectively. Given your path, return whether
or not you ever visit a point twice.
Note: You may assume you start at position (0, 0).
Ex: Given the following path…

path = "NE", return false.
Ex: Given the following path…

path = "NESW", return true.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = {(x, y)}
        for c in path:
            if c == "E":
                x += 1
            elif c == "N":
                y += 1
            elif c == "S":
                y -= 1
            elif c == "W":
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.isPathCrossing("NE") is False
    assert solution.isPathCrossing("NESW") is True
    print("All tests passed.")
