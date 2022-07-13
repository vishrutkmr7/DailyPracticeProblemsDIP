class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self, arr, left, mid, right):
        i = left
        j = mid
        k = 0
        invCount = 0
        temp = [0 for _ in range(right - left + 1)]

        while (i < mid) and (j <= right):
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1

            else:
                temp[k] = arr[j]
                invCount += mid - i
                j += 1

            k += 1
        while i < mid:
            temp[k] = arr[i]
            k += 1
            i += 1

        while j <= right:
            temp[k] = arr[j]
            k += 1
            j += 1

        for k, i in enumerate(range(left, right + 1)):
            arr[i] = temp[k]
        return invCount

    def mergeSort(self, arr, left, right):
        invCount = 0

        if right > left:
            mid = (right + left) // 2

            invCount = self.mergeSort(arr, left, mid)
            invCount += self.mergeSort(arr, mid + 1, right)
            invCount += self.merge(arr, left, mid + 1, right)

        return invCount

    def countInversions(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)
