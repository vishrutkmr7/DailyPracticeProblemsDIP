# This problem was recently asked by Uber:

# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

def findPythagoreanTriplets(nums):
    # Fill this in.
    j = 0
    n = len(nums)
    for i in range(0, (n - 2)):
        for k in range(j + 1, n): 
            for j in range(i + 1, n - 1): 
                # Calculate square of array elements 
                x = nums[i]*nums[i] 
                y = nums[j]*nums[j] 
                z = nums[k]*nums[k]  
                if (x == y + z or y == x + z or z == x + y): 
                    return True
      
    # If we reach here, no triplet found 
    return False


print (findPythagoreanTriplets([3, 12, 5, 13]))
# True