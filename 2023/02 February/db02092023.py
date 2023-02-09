"""
Given a string, text, return how many times you can form the string “programming”. 

Ex: Given the following text…

text = "mingabcprojklgram", return 1.
Ex: Given the following text…

text = "rammingabcprogrammingdefprog", return 2.
"""
from collections import Counter


class Solution:
    def count(self, text: str) -> int:
        programming = Counter("programming")
        text = Counter(text)
        return min(text[char] // programming[char] for char in programming)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.count("mingabcprojklgram"))
    print(solution.count("rammingabcprogrammingdefprog"))
