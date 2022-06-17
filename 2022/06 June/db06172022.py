"""
This question is asked by Google.
Given a string only containing the following characters (,  ), {, }, [, and ]
return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

"(){}[]", return true
"(({[]}))", return true
"{(})", return false
"""


def validate_characters(str):
    """Using stack for this problem."""
    stack = []
    for char in str:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif char in [")", "]", "}"]:
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            elif char == "]" and stack[-1] != "[":
                return False
            elif char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    return not stack


# Test Cases
print(validate_characters("(){}[]"))
print(validate_characters("(({[]}))"))
print(validate_characters("{(})"))
