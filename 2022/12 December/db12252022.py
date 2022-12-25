"""
You’re given a set of integers, dominoes, that represent a set of domino tiles. The value of domino represents either weight
and its sign, positive or negative, represents the direction it is falling: positive falls right and negative falls left.
When two dominoes collide, the larger domino destroys the smaller domino. If two dominoes of the same size collide, both
dominoes are destroyed. After all the collisions, return the state of the dominoes.

Ex: Given the following dominoes…

dominoes = [3, -3], return [].
Ex: Given the following dominoes…

dominoes = [1, 2, -3, 2, -1], return [-3, 2] (-3 destroys both dominoes to its left and the second two destroys the domino
to the right of it).
"""


class Solution:
    def pushDominoes(self, dominoes: list[int]) -> list[int]:
        # Write your code here
        if not dominoes:
            return []
        if len(dominoes) == 1:
            return dominoes
        dominoes = [0] + dominoes + [0]
        left = 0
        right = 1
        while right < len(dominoes):
            if dominoes[right] == 0:
                right += 1
                continue
            if dominoes[left] == 0:
                left = right
                right += 1
                continue
            if dominoes[left] > 0 and dominoes[right] > 0:
                dominoes[left + 1 : right] = [dominoes[left]] * (right - left - 1)
            elif dominoes[left] < 0 and dominoes[right] < 0:
                dominoes[left + 1 : right] = [dominoes[right]] * (right - left - 1)
            elif dominoes[left] > 0 and dominoes[right] < 0:
                if abs(dominoes[left]) > abs(dominoes[right]):
                    dominoes[left + 1 : right] = [dominoes[left]] * (right - left - 1)
                elif abs(dominoes[left]) < abs(dominoes[right]):
                    dominoes[left + 1 : right] = [dominoes[right]] * (right - left - 1)
                else:
                    dominoes[left + 1 : right] = [0] * (right - left - 1)
            left = right
            right += 1
        return dominoes[1:-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.pushDominoes([3, -3]) == []
    assert solution.pushDominoes([1, 2, -3, 2, -1]) == [-3, 2]
    print("All tests passed.")
