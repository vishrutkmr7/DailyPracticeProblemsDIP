# This problem was recently asked by Microsoft:

# Given a list of strings, find the longest common prefix between all strings.


def findMinLength(arr, n):
    min = len(arr[0])
    for i in range(1, n):
        if len(arr[i]) < min:
            min = len(arr[i])

    return min


def longest_common_prefix(strs):
    # Fill this in.
    n = len(strs)
    minlen = findMinLength(strs, n)
    result = ""
    for i in range(minlen):
        current = strs[0][i]

        for j in range(1, n):
            if strs[j][i] != current:
                return result

        result = result + current

    return result


print(longest_common_prefix(["helloworld", "hellokitty", "hell"]))
# hell

print(longest_common_prefix(["daily", "interview", "pro"]))
# ''
