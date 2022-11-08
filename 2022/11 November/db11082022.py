"""
Given a positive integer n, return its corresponding column title in an excel spreadsheet. 

Ex: Given the following values for n...

n = 1, return “A”.
n = 2, return “B”.
n = 3, return “C”.
n = 26, return “Z”. 
n = 27, return “AA”. 
n = 28, return “AB”. 
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            n -= 1
            result = chr(n % 26 + ord("A")) + result
            n //= 26
        return result

    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            ans += digit * 26**pos
            pos += 1

        return ans


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    assert solution.convertToTitle(1) == "A"
    assert solution.convertToTitle(2) == "B"
    assert solution.convertToTitle(3) == "C"
    assert solution.convertToTitle(26) == "Z"
    assert solution.convertToTitle(27) == "AA"
    assert solution.convertToTitle(28) == "AB"

    assert solution.titleToNumber("A") == 1
    assert solution.titleToNumber("B") == 2
    assert solution.titleToNumber("C") == 3
    assert solution.titleToNumber("Z") == 26
    assert solution.titleToNumber("AA") == 27
    assert solution.titleToNumber("AB") == 28
