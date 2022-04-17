# This problem was recently asked by Amazon:

# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.


def reverse_integer(num):
  # Fill this in.
    negativeFlag = False
    if (num < 0): 
        negativeFlag = True
        num = -num  

    prev_rev_num = 0
    rev_num = 0
    while (num != 0):  
        curr_digit = num % 10
        rev_num = (rev_num * 10) + curr_digit

        if (rev_num >= 2147483647 or 
            rev_num <= -2147483648): 
            rev_num = 0
        if ((rev_num - curr_digit) // 10 != prev_rev_num): 
            print("WARNING OVERFLOWED!!!")  
            return 0

        prev_rev_num = rev_num  
        num = num // 10


    return -rev_num if negativeFlag else rev_num
  
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
