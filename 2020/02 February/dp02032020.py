# This problem was recently asked by Apple:

# Given a number n, generate all possible combinations of n well-formed brackets.

resArr = []


def generate_brackets(n):
    # Fill this in.
    str = [""] * 2 * n
    global resArr
    resArr = []
    if n > 0:
        _printParenthesis(str, 0, n, 0, 0)

    return resArr


def _printParenthesis(str, pos, n, open, close):
    if close == n:
        resStr = ""
        for i in str:
            resStr += i
        resArr.append(resStr)
        return
    else:
        if open > close:
            str[pos] = ")"
            _printParenthesis(str, pos + 1, n, open, close + 1)
        if open < n:
            str[pos] = "("
            _printParenthesis(str, pos + 1, n, open + 1, close)


print(generate_brackets(1))
# ['()']

print(generate_brackets(3))
# ['((()))', '(()())', '()(())', '()()()', '(())()']
