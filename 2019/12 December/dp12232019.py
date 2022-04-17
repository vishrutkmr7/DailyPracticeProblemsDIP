#  This problem was recently asked by Apple:

# Given a list of words in a string, reverse the words in-place (ie don't create a new string and reverse the words).
# Since python strings are not mutable, you can assume the input will be a mutable sequence (like list).


def reverse_words(words):
    # Fill this in.
    wordArr = []
    temp = ""

    for char in words:
        if char is not " ":
            temp += char
        else:
            wordArr.append(temp)
            temp = ""

    wordArr.append(temp)  # last word
    wordArr.reverse()
    temp = "".join(f"{word} " for word in wordArr)

    return temp


s = list("can you read this")
print(reverse_words(s))
# this read you can
