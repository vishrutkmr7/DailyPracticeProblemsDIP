"""
You are given two rectangles as integer arrays and want to determine if they overlap. Each rectangle will be given as
two point, [x1, y1, x2, y2] where (x1, y1) represents the bottom-left hand corner a rectangle and (x2, y2) represents
the top-right hand corner of a rectangle. Given two arrays that represent rectangles, rect1 and rect2, return whether
or not they overlap.
Note: Two rectangles overlap if the area of their intersection is positive.

Ex: Given the two rectangles, rect1 and rect2...

rect1 = [0, 0, 1, 1], rect2 = [0, 0, 3, 3], return true.
Ex: Given the two rectangles, rect1 and rect2...

rect1 = [0, 0, 1, 1], rect2 = [1, 1, 4, 4], return false.
"""


class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return (
            rec1[0] < rec2[2]
            and rec1[1] < rec2[3]
            and rec1[2] > rec2[0]
            and rec1[3] > rec2[1]
        )


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isRectangleOverlap([0, 0, 1, 1], [0, 0, 3, 3]))
    print(solution.isRectangleOverlap([0, 0, 1, 1], [1, 1, 4, 4]))
