#  This problem was recently asked by Microsoft:

# Given a valid parenthesis string with only '(' and ')', an open parenthesis will always end with a close parenthesis,
# and a close parenthesis will never start first), remove the outermost layers of the parenthesis string and
# return the new parenthesis string.

# If the string has multiple outer layer parenthesis ie (())()), remove all outer layers and construct the new string.
# So in the example, the string can be broken down into (()) + (). By removing both components outer layer we are
# left with () + '' which is simply (), thus the answer for that input would be ().


def remove_outermost_parenthesis(S):
    # Fill this in.
    limiter = 0
    lastindex = 0
    res = []
    for i in range(len(S)):
        if limiter == 0:
            lastindex = i
        if S[i] == ")":
            limiter += 1
        if S[i] == "(":
            limiter -= 1

        if limiter == 0:
            res.append(S[lastindex + 1 : i])

    return "".join(res)


print(remove_outermost_parenthesis("(())()"))
# ()

print(remove_outermost_parenthesis("(()())"))
# ()()

print(remove_outermost_parenthesis("()()()"))
# ' '
