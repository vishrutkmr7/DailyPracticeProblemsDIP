"""
You and your friends went on a vacation. During this vacation you and your friends
paid for one another for various things like food and entertainment. For example,
Kevin might have paid $20 for Alex’s food. Now that the vacation is over,
it’s time to settle your debts. Given a list of transactions representing the
payments between people ([0, 1, 20] representing person 0 paid for person 1 $10),
return the minimum number of transactions to settle all debts.

Ex: Given the following transactions…

transactions = [[0, 1, 20]], return 1 (person 1 must pay person 0 $10 back).
Ex: Given the following transactions…

transactions = [[0, 1, 5], [0, 2, 10], [2, 1, 15]], return 2.
"""


class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        # Compute net profit for every person.
        personNetProfit = {}
        for lender, borrower, amount in transactions:
            personNetProfit[lender] = personNetProfit.get(lender, 0) - amount
            personNetProfit[borrower] = personNetProfit.get(borrower, 0) + amount
        netProfit = [amount for amount in personNetProfit.values() if amount != 0]
        return self.traverse(netProfit, 0, 0)

    def traverse(self, netProfit, startIdx, numTrans):
        # Skip settled people.
        while startIdx < len(netProfit) and netProfit[startIdx] == 0:
            startIdx += 1
        if startIdx + 1 >= len(netProfit):
            return numTrans
        for i in range(startIdx + 1, len(netProfit)):
            # Greedy condition.
            if netProfit[startIdx] + netProfit[i] == 0:
                netProfit[i] += netProfit[startIdx]
                minNumTrans = self.traverse(netProfit, startIdx + 1, numTrans + 1)
                netProfit[i] -= netProfit[startIdx]
                return minNumTrans

        minNumTrans = float("inf")
        for i in range(startIdx + 1, len(netProfit)):
            # Non-greedy condition for possible closing out in the future.
            if netProfit[startIdx] * netProfit[i] < 0:
                netProfit[i] += netProfit[startIdx]
                minNumTrans = min(
                    minNumTrans,
                    self.traverse(netProfit, startIdx + 1, numTrans + 1),
                )
                netProfit[i] -= netProfit[startIdx]
        return minNumTrans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.minTransfers([[0, 1, 20]]))
    print(solution.minTransfers([[0, 1, 5], [0, 2, 10], [2, 1, 15]]))
    print(solution.minTransfers([[0, 1, 5], [2, 3, 1], [2, 0, 1], [4, 0, 2]]))
