# This problem was recently asked by Google:

# Given a string, determine if you can remove any character to create a palindrome.


def isPalindrome(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False

        low += 1
        high -= 1

    return True


def create_palindrome(s):
    # Fill this in.
    low = 0
    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return (
                True
                if isPalindrome(s, low + 1, high)
                else bool(isPalindrome(s, low, high - 1))
            )

        low += 1
        high -= 1
    return False  # Already Palindrome


print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
