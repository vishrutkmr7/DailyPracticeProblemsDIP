"""
Given a string s containing only lowercase characters, return a list of integers representing
the size of each substring you can create such that each character in s only appears in one substring.

Ex: Given the following string s…

s = "abacdddecn", return [3, 6, 1]
Ex: Given the following string s…

s = "aba", return [3]
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels("abacdddecn"))
    print(solution.partitionLabels("aba"))
