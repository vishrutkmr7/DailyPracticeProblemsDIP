# This problem was recently asked by Apple:

# Given a string, we want to remove 2 adjacent characters that are the same, and repeat the process with the new string until we can no longer perform the operation.


def removeUtil(string, last_removed):
    if len(string) in {0, 1}:
        return string

    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]

        return removeUtil(string, last_removed)

    rem_str = removeUtil(string[1:], last_removed)

    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return rem_str[1:]

    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str

    return [string[0]] + rem_str


def remove_adjacent_dup(s):
    # Fill this in.
    last_removed = 0
    return toString(removeUtil(toList(s), last_removed))


def toList(string):
    return list(string)


def toString(x):
    return "".join(x)


print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
