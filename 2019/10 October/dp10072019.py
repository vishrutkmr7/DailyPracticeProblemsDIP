# This problem was recently asked by Google:

# Given a string with a certain rule: k[string] should be expanded to string k times.
# So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.


def decodeString(Str):
    # Fill this in.
    integerstack = []
    stringstack = []
    temp = ""
    result = ""

    for i in range(len(Str)):
        count = 0

        if Str[i] >= "0" and Str[i] <= "9":
            while Str[i] >= "0" and Str[i] <= "9":
                count = count * 10 + ord(Str[i]) - ord("0")
                i += 1

            i -= 1
            integerstack.append(count)

        elif Str[i] == "]":
            temp = ""
            count = 0

            if integerstack:
                count = integerstack[-1]
                integerstack.pop()

            while stringstack and stringstack[-1] != "[":
                temp = stringstack[-1] + temp
                stringstack.pop()

            if stringstack and stringstack[-1] == "[":
                stringstack.pop()

            for _ in range(count):
                result = result + temp

            stringstack.extend(result[j] for j in range(len(result)))
            result = ""

        elif Str[i] == "[":
            if Str[i - 1] < "0" or Str[i - 1] > "9":
                integerstack.append(1)

            stringstack.append(Str[i])

        else:
            stringstack.append(Str[i])

    while stringstack:
        result = stringstack[-1] + result
        stringstack.pop()

    return result


print(decodeString("2[a2[b]c]"))
# abbcabbc
