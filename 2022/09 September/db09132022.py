"""
This question is asked by Amazon.
You are at a birthday party and are asked to distribute cake to your guests.
Each guest is only satisfied if the size of the piece of cake they’re given,
matches their appetite (i.e. is greater than or equal to their appetite).
Given two arrays, appetite and cake where the ith element of appetite represents the ith guest’s appetite,
and the elements of cake represents the sizes of cake you have to distribute,
return the maximum number of guests that you can satisfy.

Ex: Given the following arrays appetite and cake…

appetite = [1, 2, 3], cake = [1, 2, 3], return 3.
Ex: Given the following arrays appetite and cake…

appetite = [3, 4, 5], cake = [2], return 0.
"""


class Solution:
    def maxSatisfied(self, appetite: list[int], cake: list[int]) -> int:
        appetite.sort()
        cake.sort()
        i = j = 0
        while i < len(appetite) and j < len(cake):
            if appetite[i] <= cake[j]:
                i += 1
            j += 1
        return i


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSatisfied([1, 2, 3], [1, 2, 3]))
    print(solution.maxSatisfied([3, 4, 5], [2]))
