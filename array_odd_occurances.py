#!/usr/bin/python3

"""
A non-empty array A consisting of N integers is given. The array contains
an odd number of elements, and each element of the array can be paired with
another element that has the same value, except for one element that is left
unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions,
returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""

def solution(A):
# uses a counter to detect pairs, must scan entire array
    N = len(A)

    if N == 1:
        return A[0] # returns int rather than list
    
    for i in range(N): # outer loop
        count = 0

        for x in range(N): # inner loop
            if A[i] == A[x]:
                count += 1 # counts matches
        
        if count == 1:
            return A[i]

    return 0 # fallback for unexpected cases - checker did have an array without unpaired int
"""
efficiency low (O(N**2))for large arrays here, carks it for large arrays
see alt solution below
"""

"""
This XOR ("Exclusive or") application uses an instantaneous mathematical
application to eliminate all pairs and return the unpaired value.
At O(n) this is the most efficient solution
This would NOT work if there were multiple unpaired values
"""
def solutionB(A):
    result = 0
    for x in A:
        result ^= x
    return result

# generic array
print(f"input [7, 1, 1, 2, 2] solution {solution([7, 1, 1, 2, 2])}")
print(f"input [7, 1, 1, 2, 2] solutionB {solutionB([7, 1, 1, 2, 2])}")
# single element array
print(f"input [7] solution {solution([7])}")
print(f"input [7] solutionB {solutionB([7])}")
# small array, unpaired element at end
print(f"input [2, 2, 3] solution {solution([2, 2, 3])}")
print(f"input [2, 2, 3] solutionB {solutionB([2, 2, 3])}")
# negative unpaired element
print(f"input [2, 2, -5] solution {solution([2, 2, -5])}")
print(f"input [2, 2, -5] solutionB {solutionB([2, 2, -5])}")
# unpaired element surrounded by many pairs
print(f"input [9, 3, 9, 3, 9, 7, 9] solution {solution([9, 3, 9, 3, 9, 7, 9])}")
print(f"input [9, 3, 9, 3, 9, 7, 9] solutionB {solutionB([9, 3, 9, 3, 9, 7, 9])}")
# large integer
print(f"input [1000000000, 1, 1] solution {solution([1000000000, 1, 1])}")
print(f"input [1000000000, 1, 1] solutionB {solutionB([1000000000, 1, 1])}")