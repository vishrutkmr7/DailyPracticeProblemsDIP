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
    This is a somewhat optimal solution.
    """
    if len(jewels) == 0 or len(stones) == 0:
        return 0
    return sum(stone in jewels for stone in stones)


# Test Cases
print(num_jewel_stones("abc", "ac"))
print(num_jewel_stones("Af", "AaaddfFf"))
print(num_jewel_stones("AYOPD", "ayopd"))
