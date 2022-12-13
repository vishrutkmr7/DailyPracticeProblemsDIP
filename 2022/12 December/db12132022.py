"""
You are given n pairs of numbers and asked to form a chain. Two pairs of numbers can create a link in
the chain if the second number in the first pair is less than the first number in the second pair.
Return the length of the longest chain you can form.
Note: You may use the pairs of numbers in any order and the first number in a pair is always less than
the second number in a pair.

Ex: Given the following pairs...

pairs = [[3,4], [5, 6], [7, 8]], return 3.
Ex: Given the following pairs...

pairs = [[9, 14], [3, 5], [4, 7]], return 2.
"""


class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        prev = float("-inf")
        for pair in pairs:
            if pair[0] > prev:
                count += 1
                prev = pair[1]
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.findLongestChain([[3, 4], [5, 6], [7, 8]]))
    print(solution.findLongestChain([[9, 14], [3, 5], [4, 7]]))
