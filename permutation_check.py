"""
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from
1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:
    def solution(A)
that, given an array A, returns 1 if array A is a permutation
and 0 if it is not.

If the function is a permutation, it should return 1.
If it is not, the function should return 0.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [1..1,000,000,000].
"""

"""
My first crack - use solutionB for better efficiency
This got 33% performance - O(N^2)
"""
def solution(A):
    orig_length = len(A)

    for num in range(1, orig_length + 1):
        if num not in A:
            return 0
    return 1

"""
This is the one you want to use
Efficiency is O(n) and logic is better
1. Check if array length is the same after converting to a set (which removes duplicates)
2. Check if the highest number in the array is equal to the length, because if they are
all unique values then the final number in a sequence of fixed length will be equal to n
"""

def solutionB(A):
    N = len(A)
    seen = set(A) # won't accept duplicates
    return 1 if len(seen) == N and max(seen) == N and min(seen) == 1 else 0

