"""
This question is asked by Amazon.
Given a string representing your stones and another string representing a list of jewels,
return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0
"""


def num_jewel_stones(jewels, stones):
    """
    This is a brute force solution.
    """
    if len(jewels) == 0 or len(stones) == 0:
        return 0
    if len(jewels) == 1:
        return stones.count(jewels)
    if len(stones) == 1:
        return jewels.count(stones)
    for i in range(len(jewels)):
        for j in range(len(stones)):
            if jewels[i] == stones[j]:
                return 1 + num_jewel_stones(jewels, stones[j + 1 :])
    return 0


# Test Cases
print(num_jewel_stones("abc", "ac"))
print(num_jewel_stones("Af", "AaaddfFf"))
print(num_jewel_stones("AYOPD", "ayopd"))
