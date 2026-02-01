#!/usr/bin/python3

"""
An array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)], which
means that exactly one element is missing.
Your goal is to find that missing element.

Write a function:
    def solution(A)
that, given an array A, returns the value of the missing element.

For example, given array A such that:
    A[0] = 2
    A[1] = 3
    A[2] = 1
    A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [0..100,000];
    the elements of A are all distinct;
    each element of array A is an integer within the range [1..(N + 1)].
"""
def solution(A):
# reminder: XOR cancels out matching variables  
    N = len(A)
    xor_all = 0 # empty variable

    for i in range(1, N + 2): # remember range STOP is exclusive
        xor_all ^= i # XOR on 1 to N+1, variable takes all numbers as no pairs exist

    for num in A:
        xor_all ^= num # XOR variable numbers with Array, only the missing number remains

    return xor_all


def solutionB(A):
    N = len(A)
    expected = (N + 1) * (N + 2) // 2
    actual = sum(A)
    return expected - actual

"""
This is a mathey solution that requires you to remember the formula.
It is a clever solution but XOR is probably preferable under
a time constraint.

Example
A = [1, 2, 5, 4, 6] sum = 18
so N = 5, which means N+1 = 6 and N+2 = 7
(N + 1) * (N + 2) = 42
42 / 2 = 21
21(expected) - 18(actual) = 3
"""