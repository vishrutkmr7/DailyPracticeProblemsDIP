# This problem was recently asked by Amazon:

# Given a string, return the first recurring letter that appears. If there are no recurring letters, return None.


def first_recurring_char(s):
    # Fill this in.
    stack = []
    for i in s:
        if i in stack:
            return i
        else:
            stack.append(i)

    return None


print(first_recurring_char("qwertty"))
# t

print(first_recurring_char("qwerty"))
# None
