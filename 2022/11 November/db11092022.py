"""
You are given two integer arrays top and bottom that represent the top and bottom halves
of dominoes respectively. Return the minimum number of rotations (i.e. the top value becomes
the bottom value of the domino and the bottom value becomes the top value of the domino) 
ou need to perform to make all the values in top the same or all the values in bottom the same.
Note: If it is not possible to make all the values in top or bottom the same, return -1.

Ex: Given the following top and bottom...

top = [2,1,2,4,2,2], bottom = [5,2,6,2,3,2], return 2.
We can rotate the second and fourth dominoes to make all values in the top row of our dominoes equal.
"""


class Solution:
    def minDominoRotations(self, top: list[int], bottom: list[int]) -> int:
        n = len(top)
        for x in range(1, 7):
            top_count = 0
            bottom_count = 0
            for i in range(n):
                if top[i] != x and bottom[i] != x:
                    break
                elif top[i] != x:
                    top_count += 1
                elif bottom[i] != x:
                    bottom_count += 1
            else:
                return min(top_count, bottom_count)
        return -1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
