"""
You are given an integer array, magnets where each value in the array represents the size of a particular magnet.
You goal is to connect all the magnets together to form a single magnet. Every time you connect two magnets, a and b
together, you pay a cost of a + b. Return the minimum cost to connect all the magnets together.

Ex: Given the following magnets…

magnets = [1, 2, 3], return 9 (add 1 and 2 together for a cost of 3, add 3 and 3 together for a total cost of 6,
summing these costs together we get 9).
Ex: Given the following magnets…

magnets = [5, 2, 4, 1], return 22.
"""


import heapq


class Solution:
    def connectMagnets(self, magnets: list[int]) -> int:
        minCost = 0
        heapq.heapify(magnets)
        while len(magnets) > 1:
            cost = heapq.heappop(magnets) + heapq.heappop(magnets)
            heapq.heappush(magnets, cost)
            minCost += cost
        return minCost


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.connectMagnets([1, 2, 3]))
    print(solution.connectMagnets([5, 2, 4, 1]))
