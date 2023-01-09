"""
Given a string array, words, return a list containing all the characters that are common to all the words.
Note: If a character appears multiple times in all the words it should also appear multiple times in your return list.

Ex: Given the following words…

words = ["abc", "ab", "a"], return ["a"].
Ex: Given the following words…

words = ["deef", "ddabee", "eebhk"], return ["e","e"].
"""


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = []
        for i in words[0]:
            if all(i in word for word in words):
                result.append(i)
                words = [word.replace(i, "", 1) for word in words]
        return result


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.commonChars(["abc", "ab", "a"]))
    print(solution.commonChars(["deef", "ddabee", "eebhk"]))
