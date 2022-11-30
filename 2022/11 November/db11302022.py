"""
Given a paragraph and a list of banned words, return the most frequently occurring word that is
not banned. Treat words case insensitively and ignore punctuation.

Ex: Given the following paragraph and list of banned words...

paragraph = "The daily, the byte Daily.", banned = [“the”], return “daily”.
"""

import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        ban = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        return Counter(w for w in words if w not in ban).most_common(1)[0][0]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.mostCommonWord(
            "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
        )
    )
    print(solution.mostCommonWord("The daily, the byte Daily.", ["the"]))
