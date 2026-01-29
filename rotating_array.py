#!/usr/bin/python3

"""
An array A consisting of N integers is given. Rotation of the array means that 
each element is shifted right by one index, and the last element of the array 
is moved to the first place. For example, the rotation of 
array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one 
index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted 
to the right K times.

Write a function:
    def solution(A, K)
that, given an array A consisting of N integers and an integer K, returns the 
array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
    the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given
    A = [0, 0, 0]
    K = 1
    the function should return [0, 0, 0]
Given
    A = [1, 2, 3, 4]
    K = 4
    the function should return [1, 2, 3, 4]

Assume that:
- N and K are integers within the range [0..100];
- each element of array A is an integer within the range [−1,000..1,000].
- In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

Notes;
N = number of ints
A = array
K = number of steps/rotations
"""

def solution(A, K):
    N = len(A) # total number of ints

    if N == 0:
        return A
    if  K == 0 or K == N:
        return A

    K = (K % N) 
    # remainder of modulo gives us the rotation numbers 
    # remaining after one or more full rotations, so (10 % 6 has remainder 4)

    base = A[:(N - K)] # slice to keep ints remaining in position
    mover = A[(N - K):] # slice to keep ints being moved to front of array

    return mover + base

# Tests
print(f"1. (2) original: [1, 2, 3, 4, 5, 6] solution: {solution([1, 2, 3, 4, 5, 6], 2)}") # K = 1
print(f"2. (3) original: [3, 8, 9, 7, 6] solution: {solution([3, 8, 9, 7, 6], 3)}") # K = 3
print(f"3. (1) original: [0, 0, 0] solution: {solution([0, 0, 0], 1)}") # identical items in array
print(f"4. (4) original: [1, 2, 3, 4] solution: {solution([1, 2, 3, 4], 4)}") # K == N
print(f"5. (3) original: [-1000, -400, -140, 200, 2000] solution: {solution([-1000, -400, -140, 200, 2000], 3)}") # negative numbers in array
print(f"6. (2) original: [] solution: {solution([], 2)}") # no ints in array
print(f"7. (2) original: [5] solution: {solution([5], 2)}") # only one int in array
print(f"8. (0) original: [5] solution: {solution([5], 0)}") # K = 0
print(f"9. (0) original: [1, 2, 3, 4, 5, 6] solution: {solution([1, 2, 3, 4, 5, 6], 0)}") # K = 0
print(f"10. (10) original: [1, 2, 3, 4, 5, 6] solution: {solution([1, 2, 3, 4, 5, 6], 10)}") # K larger than N