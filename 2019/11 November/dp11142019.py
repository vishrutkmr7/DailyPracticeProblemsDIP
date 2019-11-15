#  This problem was recently asked by Uber:

# You are given a list of n numbers, where every number is at most k indexes away from its properly sorted index.
# Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)


from heapq import heappop, heappush, heapify


def sort_partially_sorted(nums, k):
    # Fill this in.
    n = len(nums)
    heap = nums[: k + 1]
    heapify(heap)
    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        nums[target_index] = heappop(heap)
        heappush(heap, nums[rem_elmnts_index])
        target_index += 1

    while heap:
        nums[target_index] = heappop(heap)
        target_index += 1
    return nums


print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]

