# # https://www.codechef.com/JAN20B/problems/BRKBKS
# For her next karate demonstration, Ada will break some bricks.

# Ada stacked three bricks on top of each other. Initially, their widths (from top to bottom) are W1,W2,W3.
# Ada's strength is S. Whenever she hits a stack of bricks, consider the largest k≥0 such that the sum of widths of the topmost k bricks does not exceed S;
# the topmost k bricks break and are removed from the stack. Before each hit, Ada may also decide to reverse the current stack of bricks, with no cost.
# Find the minimum number of hits Ada needs in order to break all bricks if she performs the reversals optimally. You are not required to minimise the number of reversals.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains four space-separated integers S, W1, W2 and W3.

# Output
# For each test case, print a single line containing one integer ― the minimum required number of hits.

# Constraints
# 1≤T≤64
# 1≤S≤8
# 1≤Wi≤2 for each valid i
# it is guaranteed that Ada can break all bricks
# Subtasks
# Subtask #1 (50 points): W1=W2=W3
# Subtask #2 (50 points): original constraints

# Example Input
# 3
# 3 1 2 2
# 2 1 1 1
# 3 2 2 1
# Example Output
# 2
# 2
# 2


def strike(S, bricks):
    sumB = 0

    for b in bricks:
        sumB += b
        if sumB <= S:
            bricks.pop(0)
        else:
            break

    return bricks


def no_of_hits(strength, bricks):
    # Fill this in
    count = 0
    while len(bricks) > 0:
        bricks = strike(strength, bricks)
        count += 1
 
    return count


print(no_of_hits(3, [1, 2, 2]))
# 2
print(no_of_hits(2, [1, 1, 1]))
# 2
print(no_of_hits(3, [2, 2, 1]))
# 2
