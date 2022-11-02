"""
Given an array of words, return the length of the longest phrase, containing only unique characters,
that you can form by combining the given words together.

Ex: Given the following words…

words = ["the","dog","ran"], return 9 because you can combine all the words, i.e.
"the dog ran" since all the characters in the phrase are unique.
Ex: Given the following words…

words = ["the","eagle","flew"], return 4 because "flew" is the longest phrase you can create
without using duplicate characters.
"""


class Solution:
    def longestUniquePhrase(self, words: list[str]) -> int:
        dp = [set()]
        for word in words:
            if len(set(word)) < len(word):
                continue
            word = set(word)
            dp.extend(word | entry for entry in dp[:] if not word & entry)
        return max(len(word) for word in dp)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestUniquePhrase(["the", "dog", "ran"]))
    print(solution.longestUniquePhrase(["the", "eagle", "flew"]))
