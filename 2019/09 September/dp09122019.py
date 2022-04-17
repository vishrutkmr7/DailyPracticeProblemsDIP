# This problem was recently asked by Amazon:

# You are given a string s, and an integer k.
# Return the length of the longest substring in s that contains at most k distinct characters.

MAX_CHARS = 26


def isValid(count, k):
    val = sum(count[i] > 0 for i in range(MAX_CHARS))
    # Return true if k is greater than or equal to val
    return k >= val


def longest_substring_with_k_distinct_characters(s, k):
    # Fill this in.
    u = 0  # number of unique characters
    n = len(s)

    count = [0] * MAX_CHARS
    for i in range(n):
        if count[ord(s[i]) - ord("a")] == 0:
            u += 1
        count[ord(s[i]) - ord("a")] += 1

    if u < k:
        print("Not enough unique characters")
        return

    curr_start = 0
    curr_end = 0
    max_window_size = 1
    max_window_start = 0
    count = [0] * len(count)
    count[ord(s[0]) - ord("a")] += 1

    for i in range(1, n):
        count[ord(s[i]) - ord("a")] += 1
        curr_end += 1

        while not isValid(count, k):
            count[ord(s[curr_start]) - ord("a")] -= 1
            curr_start += 1

        if curr_end - curr_start + 1 > max_window_size:
            max_window_size = curr_end - curr_start + 1
            max_window_start = curr_start

    return (
        str(max_window_size)
        + " (because '"
        + s[max_window_start:]
        + "' has length "
        + str(max_window_size)
        + " with "
        + str(k)
        + " characters)"
    )


print(longest_substring_with_k_distinct_characters("aabcdefff", 3))
# 5 (because 'defff' has length 5 with 3 characters)
