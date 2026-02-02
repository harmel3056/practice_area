#!/usr/bin/python3

"""
You are given N counters, initially set to 0, and you have two possible
operations on them:
    increase(X) - counter X is increased by 1,
    max counter - all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:
    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:
    def solution(N, A)
that, given an integer N and a non-empty array A consisting of M integers,
returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:
    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:
    N and M are integers within the range [1..100,000];
    each element of array A is an integer within the range [1..N + 1].
"""

def solution(N, A):
    counter = [0] * N # [0, 0, 0, 0, 0] for N = 5
    baseline = 0 # brings counter up to base when incrementing, and saves universal max update for the end
    current_max = 0 # tracks true maximum counter value without rescanning the array

    for X in A: # will iterate once for every array item
        if 1 <= X <= N:
            idx = X - 1 # corrects for array[idx] starting at 0, counter ID starts at 1: "1 <= X <= N"

            if counter[idx] < baseline: # brings value up to baseline if not already there
                counter[idx] = baseline
            
            counter[idx] += 1 # increment counter

            if counter[idx] > current_max: # update max without having to scan array
                current_max = counter[idx]
        
        else:
            baseline = current_max # ensures future iterations are based on the current max count
    
    for J, K in enumerate(counter): # brings any values below the max up to that baseline at the end
        if K < baseline:
            counter[J] = baseline

    return counter

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
