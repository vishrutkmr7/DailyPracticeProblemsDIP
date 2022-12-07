"""
You are given a string S (that consists of only alphanumerical characters) and asked to reformat it
into a gift card code. S has N dashes that separates the string into N + 1 groups of characters.
Every gift card code needs to contain all uppercase characters and have exactly K characters in
each group, except the first group (but the first group must have at least one character).
Given S, reformat it into a gift card code and return the result.

Ex: Given the following values of S and K...

S = “49DkeDb39LXI”, K = 3, return "49D-KED-B39-LXI".
Ex: Given the following values of S and K...

S = “9Dklsi3nsEKE92”, K = 3 return "9D-KLS-I3N-SEK-E92".
"""


class Solution:
    def reformat(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()
        result = ""
        for i, v in enumerate(S[::-1]):
            if i % K == 0 and i != 0:
                result += "-"
            result += v
        return result[::-1]


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.reformat("49DkeDb39LXI", 3))
    print(sol.reformat("9Dklsi3nsEKE92", 3))
