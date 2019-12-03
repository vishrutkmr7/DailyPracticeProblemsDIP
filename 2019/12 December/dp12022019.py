# This problem was recently asked by Facebook:

# Given an expression (as a list) in reverse polish notation, evaluate the expression.
# Reverse polish notation is where the numbers come before the operand. Note that there can be the 4 operands '+', '-', '*', '/'.
# You can also assume the expression will be well formed.

ops = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
}


def reverse_polish_notation(expr):
    # Fill this in.
    stack = []
    for token in expr:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()


# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, "+", 2, "*", "-"]))
# -9
