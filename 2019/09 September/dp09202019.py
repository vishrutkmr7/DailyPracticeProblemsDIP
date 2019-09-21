#  This problem was recently asked by Uber:

# You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed
# in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.


def count_invalid_parenthesis(string):
    # Fill this in.
    op = 0
    close = 0
    for ch in string:
        if ch == "(":
            op += 1
        elif ch == ")":
            close += 1

    return max(op, close) - min(op, close)


print(count_invalid_parenthesis("()())()"))
# 1
