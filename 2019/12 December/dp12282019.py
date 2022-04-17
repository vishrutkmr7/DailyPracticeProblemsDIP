# em was recently asked by AirBNB:

# The power function calculates x raised to the nth power.
# If implemented in O(n) it would simply be a for loop over n and multiply x n times.
# Instead implement this power function in O(log n) time. You can assume that n will be a non-negative integer.


def pow(x, n):
  # Fill this in.
    if(n == 0): return 1
    temp = pow(x, int(n / 2))  

    if (n % 2 == 0): 
        return temp * temp
    else: 
        return x * temp * temp if (n > 0) else (temp * temp) / x 

print(pow(5, 3))
# 125
