# This problem was recently asked by Google:

# Given two strings, find if there is a one-to-one mapping of characters between the two strings.


def has_character_map(str1, str2):
    # Fill this in.
    if len(str1) != len(str2):
        return False
    k = ord(str2[0]) - ord(str1[0])  # Improve k calc

    for i in range(0, len(str1)):
        if not (ord(str1[i]) + k == ord(str2[i])):
            return False

    return True


print(has_character_map("abc", "def"))
# True
print(has_character_map("aac", "def"))
# False
