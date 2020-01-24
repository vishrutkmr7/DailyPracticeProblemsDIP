# This problem was recently asked by Twitter:

# Given 3 sorted lists, find the intersection of those 3 lists.


def intersection(list1, list2, list3):
    # Fill this in.
    return list(set(list1) & set(list2) & set(list3))


print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
