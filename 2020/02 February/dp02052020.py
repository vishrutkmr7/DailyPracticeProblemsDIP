# This problem was recently asked by Twitter:

# Given a list of numbers and a target number, find all possible unique subsets of the list of numbers that sum up to the target number. The numbers will all be positive numbers.
res = []


def unique_combination(l, sum, K, local, A):
    if sum == K:
        res.append(tuple(local))
        return

    for i in range(l, len(A), 1):
        if sum + A[i] > K:
            continue

        if i == 1 and A[i] == A[i - 1] and i > l:
            continue

        local.append(A[i])

        unique_combination(i + 1, sum + A[i], K, local, A)

        local.remove(local[len(local) - 1])


def sum_combinations(nums, target):
    # Fill this in.
    nums.sort(reverse=False)
    local = []

    unique_combination(0, 0, target, local, nums)
    return res


print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
