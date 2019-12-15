# This problem was recently asked by AirBNB:

# Given a phone number, return all valid words that can be created using that phone number.


lettersMaps = {
    1: [],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
    0: [],
}

validWords = ["dog", "fish", "cat", "fog"]


def makeWords(phone):
    # Fill this in
    ret = [""]
    for digit in phone:
        letters = lettersMaps[int(digit)]
        ret = [prefix + letter for prefix in ret for letter in letters]

    return [r for r in ret if r in validWords]


print(makeWords("364"))
# ['dog', 'fog']
