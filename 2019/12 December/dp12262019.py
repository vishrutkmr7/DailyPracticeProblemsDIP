# This problem was recently asked by LinkedIn:

# Given a string, convert it to an integer without using the builtin str function.
# You are allowed to use ord to convert a character to ASCII code.

# Consider all possible cases of an integer. In the case where the string is not a valid integer, return None.


def convert_to_int(s):
    # Fill this in.
    result = 0
    if not s.isnumeric:
        return None

    for digit in s:
        result *= 10
        for d in "0123456789":
            result += digit > d

    return result if s[0] is not "-" else -result


print(convert_to_int("-105") + 1)
# -104
