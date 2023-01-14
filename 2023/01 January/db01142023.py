"""Given a string s and an integer array, indices, you must rearrange s according to the given indices.
Once you have rearranged s successfully, the ith character in s should now be located at the indices[i]
index.
Note: s and indices will always be the same length. 

Ex: Given the following s and indices…

s = "abc", indices = [2, 1, 0], return "cba" ('a' moves to the 2nd index, b stays at the first index,
and c moves to the zeroth index).
"""


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        return "".join([s[indices.index(i)] for i in range(len(s))])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreString("abc", [2, 1, 0]))
    print(solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
