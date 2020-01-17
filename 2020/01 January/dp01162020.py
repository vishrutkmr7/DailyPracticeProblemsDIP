# This problem was recently asked by Facebook:

# Given a numerator and a denominator, find what the equivalent decimal representation is as a string. If the decimal representation has recurring digits,
# then put those digits in brackets (ie 4/3 should be represented by 1.(3) to represent 1.333...). Do not use any built in evaluator functions like python's eval.
# You can also assume that the denominator will be nonzero.


def frac_to_dec(numerator, denominator):
    # Fill this in.
    result = [str(numerator // denominator) + "."]
    subresults = [numerator % denominator]
    numerator %= denominator
    while numerator != 0:
        numerator *= 10
        result_digit, numerator = divmod(numerator, denominator)
        result.append(str(result_digit))

        if numerator not in subresults:
            subresults.append(numerator)

        else:
            result.insert(subresults.index(numerator) + 1, "(")
            result.append(")")
            break
    return "".join(result)


print(frac_to_dec(3, 2))
# 1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)
