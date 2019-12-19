# This problem was recently asked by Amazon:

# Given a string that may represent a number, determine if it is a number. Here's some of examples of how the number may be presented.


def parse_number(s):
    # Fill this in.
    try:
        val = int(s)
    except ValueError:
        try:
            val = float(s)
        except ValueError:
            return False

    return True


print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False
