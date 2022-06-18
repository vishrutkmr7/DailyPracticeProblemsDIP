"""
This question is asked by Amazon.
Given two strings s and t, which represents a sequence of keystrokes,
where # denotes a backspace,
return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false
"""


def prep_stack(string):
    """Using stack for this problem."""
    stack = []
    for char in string:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return stack


def compare_keystrokes(s, t):
    """Using stack for this problem."""
    stack_s = prep_stack(s)
    stack_t = prep_stack(t)
    return stack_s == stack_t


# Test Cases
print(compare_keystrokes("ABC#", "CD##AB"))
print(compare_keystrokes("como#pur#ter", "computer"))
print(compare_keystrokes("cof#dim#ng", "code"))
