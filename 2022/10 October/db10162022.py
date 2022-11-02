"""
Given a list of words, return the top k frequently occurring words.
Note: If two words occur with the same frequency, then the alphabetically smaller word should come first.
Ex: Given the following words and value k…

words = ["the", "daily", "byte", "byte"], k = 1, return ["byte"].
Ex: Given the following words and value k…

words = ["coding", "is", "fun", "code", "coding", "fun"], k = 2, return ["coding","fun"].
"""


from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = Counter(words)
        return [x[0] for x in sorted(counts.items(), key=lambda x: (-x[1], x[0]))][:k]
