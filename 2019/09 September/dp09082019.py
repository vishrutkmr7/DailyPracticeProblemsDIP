# This problem was recently asked by Google:

# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term
# is obtained by describing the previous term. An example is easier to understand:

# Each consecutive value describes the prior value.

# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

# Your task is, return the nth term of this sequence. (P.S. It's also called the Conway Sequence)


def lookandsay(n):
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 11
    s = "11"
    for _ in range(3, n + 1):
        s += "$"
        l = len(s)
        cnt = 1  # Count of matching chars
        tmp = ""  # ith term
        for j in range(1, l):
            # Current char isn't matching
            if s[j] != s[j - 1]:
                tmp += str(cnt + 0)
                tmp += s[j - 1]
                cnt = 1  # reset count
            else:
                cnt += 1
        s = tmp
    return s


# Driver code
for i in range(1, 10):
    print(lookandsay(i))
