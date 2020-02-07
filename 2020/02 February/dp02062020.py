# This problem was recently asked by Twitter:

# Given a sorted list with duplicates, and a target number n, find the range in which the number exists
# (represented as a tuple (low, high), both inclusive. If the number does not exist in the list, return (-1, -1)).


def getIndexPositions(listOfElements, element):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = listOfElements.index(element, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break

    return indexPosList


def find_num(nums, target):
    # Fill this in.
    # if not sorted, else add uptill the end of occurences for sorted
    index = getIndexPositions(nums, target)
    if index == []:
        return (-1, -1)

    return (min(index), max(index))


print(find_num([1, 1, 3, 5, 7], 1))
# (0, 1)

print(find_num([1, 2, 3, 4], 5))
# (-1, -1)

