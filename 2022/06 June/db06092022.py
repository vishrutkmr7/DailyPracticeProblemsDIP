"""
This question is asked by Amazon.
Given two strings representing sentences, return the words that are not common to both strings
(i.e. the words that only appear in one of the sentences).
You may assume that each sentence is a sequence of words (without punctuation)
correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the hare", sentence2 = "the tortoise lost to the hare", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""


def uncommon_words(sentence1, sentence2):
    """
    This is an optimal solution.
    """
    words1 = sentence1.split()
    words2 = sentence2.split()
    return list(set(words1) ^ set(words2))


# Test Cases
print(uncommon_words("the quick", "brown fox"))
print(uncommon_words("the tortoise beat the hare", "the tortoise lost to the hare"))
print(uncommon_words("copper coffee pot", "hot coffee pot"))
