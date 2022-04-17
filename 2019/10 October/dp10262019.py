# This problem was recently asked by Apple:

# You are given two strings, A and B. Return whether A can be shifted some number of times to get B


def is_shifted(a, b):
    # Fill this in.
    if len(a) != len(b):
        return False

    clock_rot = ""
    anticlock_rot = ""
    l = len(b)

    # Initialize string as anti-clockwise rotation
    anticlock_rot = anticlock_rot + b[l - 2 :] + b[:l - 2]

    # Initialize string as clock wise rotation
    clock_rot = clock_rot + b[2:] + b[:2]

    # check if any of them is equal to string1
    return a in [clock_rot, anticlock_rot]


print(is_shifted("abcde", "cdeab"))
# True
print(is_shifted("abc", "acb"))
# False
