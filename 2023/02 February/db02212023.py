"""
Given an array of words and a string of characters, chars, return the sum of the lengths of words that can be formed
using only the chars.
Note: Each character within chars can only be used once.

Ex: Given the following words and chars…

words = ["abc", "cab"], chars = "bac", return 6 ("abc"'s length + "cab"'s length).
"""


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = 0
        for word in words:
            flag = all(word.count(i) <= chars.count(i) for i in word)
            if flag:
                count += len(word)
        return count


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.countCharacters(["abc", "cab"], "bac"))
