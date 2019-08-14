# This problem was recently asked by AirBNB:

# Given two strings, determine the edit distance between them.
# The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

def distance(s1, s2):
    # Fill this in.
    m = len(s1)
    n = len(s2)

    # Empty strings: if one of them is empty => insert all characters of the other
    if m == 0:
        return n
    elif n == 0:
        return m

    # If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. 
    if s1[m-1] == s2[n-1]: 
        return distance(s1[:-1], s2[:-1])

    # If last characters are not same, consider all three operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take minimum of three values. 
    return 1 + min(distance(s1, s2[:-1]), # Insert
        distance(s1[:-1], s2), # Remove
        distance(s1[:-1], s2[:-1])) # Replace
           
print (distance('biting', 'sitting'))
# 2