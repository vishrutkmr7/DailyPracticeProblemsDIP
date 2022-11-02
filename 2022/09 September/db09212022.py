"""
Given a string s, return all of its repeated 10 character substrings.
Note: You may assume s only contains uppercase alphabetical characters.

Ex: Given the following string s…

s = "BBBBBBBBBBB", return ["BBBBBBBBBB"].
Ex: Given the following string s…

s = "ABABABABABABBBBBBBBBBB", return ["ABABABABAB","BBBBBBBBBB"].
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub in seen:
                repeated.add(sub)
            seen.add(sub)
        return list(repeated)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    # Example 1
    s = "BBBBBBBBBBB"
    print(solution.findRepeatedDnaSequences(s))

    # Example 2
    s = "ABABABABABABBBBBBBBBBB"
    print(solution.findRepeatedDnaSequences(s))
