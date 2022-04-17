# This problem was recently asked by Facebook:

# Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit number
# that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.
# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.
# Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant


KAPREKAR_CONSTANT = 6174


def kaprekar(n):
    ascending = "".join(sorted(str(n)))
    descending = "".join(sorted(str(n), reverse=True))
    # Padding
    if len(descending) != 4:
        p = 4 - len(descending)
        ad = "".join("0" for _ in range(p))
        descending += ad
    return int(descending) - int(ascending)


def num_kaprekar_iterations(n):
    # Fill this in.
    count = 1
    kap = kaprekar(n)
    while kap != KAPREKAR_CONSTANT:
        kap = kaprekar(kap)
        count += 1

    return count


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
