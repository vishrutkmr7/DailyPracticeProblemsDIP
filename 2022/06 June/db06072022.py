"""
This question is asked by Google.
You are given two strings, s and t which only consist of lowercase letters.
t is generated by shuffling the letters in s as well as potentially adding an additional random character.
Return the letter that was randomly added to t if it exists, otherwise, return ’  ‘. 
Note: You may assume that at most one additional character can be added to t. 

Ex: Given the following strings...

s = "foobar", t = "barfoot", return 't'
s = "ide", t = "idea", return 'a'
s = "coding", t "ingcod", return ""
"""


def spot_the_difference(s, t):
    """
    This is an optimal solution.
    """
    return [i for i in t if i not in s][0] if len(t) > len(s) else ""


# Test Cases
print(spot_the_difference("foobar", "barfoot"))
print(spot_the_difference("ide", "idea"))
print(spot_the_difference("coding", "ingcod"))
