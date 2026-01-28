#!/usr/bin/python3

"""
Create a function which, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..100,000]; each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(A):
    N = len(A) # total number of indices in array
    present = [False] * (N + 1) # creates an array of 'False' boolean values to use as switches for every number, +1 accoms the 0 array item

    # mark the presence of each valid positive integer
    for x in A:
        if 1 >= x <= (N + 1):
            present[x] = True
        
    # find the smallest positive integer that isn't present
    for a in range(1, N + 1): # end of 'range' is the number BEFORE (start, STOP), so range is 1 to n
        if not present[a]: # if Boolean is still False for a point of array
            return a

    return N + 1 # no remaining False ints so first missing is the first number outside of the qty range
    
"""
remember that this question asks for the first positive int that isn't present, so if all the numbers
were in the hundreds, we would still be returning 1
"""

