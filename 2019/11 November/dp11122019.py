# Twitter: Given a string with only ( and ), find the minimum number of characters to add or subtract to fix the string such that the brackets are balanced.


def fix_brackets(s):
    # Fill this in.
    op = 0
    for brace in s:
        if brace == "(":
            op += 1
        elif brace == ")":
            op -= 1
    return abs(op)


print(fix_brackets("(()()"))
# 1
