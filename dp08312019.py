# This problem was recently asked by Apple:

# You are given an array. Each element represents the price of a stock on that particular day.
# Calculate and return the maximum profit you can make from buying and selling that stock only once.


def buy_and_sell(arr):
    # Fill this in.
    maxP = -1
    buy = 0
    sell = 0

    change = True  # Loop control

    for i in range(0, len(arr) - 1):
        sell = arr[i + 1]

        if change:
            buy = arr[i]

        if sell < buy:
            change = True
            continue
        else:
            temp = sell - buy
            if temp > maxP:
                maxP = temp
            change = False

    return maxP


print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
