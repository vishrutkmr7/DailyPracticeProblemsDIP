# This problem was recently asked by AirBNB:

# Given a non-empty list of words, return the k most frequent words.
# The output should be sorted from highest to lowest frequency, and if two words have the same frequency,
# the word with lower alphabetical order comes first. Input will contain only lower-case letters.


class Solution(object):
    def topKFrequent(self, words, k):
        # Fill this in.
        wordDict = {}
        for word in words:
            if word.lower() not in wordDict.keys():
                wordDict[word.lower()] = 1
            else:
                wordDict[word.lower()] += 1
        sortWord = sorted(wordDict.items(), key=lambda x: x[1])
        sortWord.reverse()
        ans = []
        for i in range(0, k):
            (word, count) = sortWord[i]
            ans.append(word)

        return ans


words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
