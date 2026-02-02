#!/usr/bin/python3

"""
A non-empty array A consisting of N integers is given. 
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty
parts: A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N - 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|

In other words, it is the absolute difference between the sum of the
first part and the sum of the second part.

For example, consider array A such that:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
We can split this tape in four places:
    P = 1, difference = |3 - 10| = 7
    P = 2, difference = |4 - 9| = 5
    P = 3, difference = |6 - 7| = 1
    P = 4, difference = |10 - 3| = 7
Write a function:
    def solution(A)
that, given a non-empty array A of N integers, returns the minimal 
difference that can be achieved.

For example, given:
    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 4
    A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [2..100,000];
    each element of array A is an integer within the range [-1,000..1,000].
"""

def solution(A):
    N = len(A)
    total_sum = sum(A)
    left_side = 0
    
    differences = []

    for x in range(0,(N - 1)): # N - 1 is the limit so that is the count we use for iterations
        left_side += A[x] # increases sum with additon of x on each iteration, adds x & x+1, x+2 so forth
        right_side = total_sum - left_side # decreases as left_side increases
        
        difference = abs(right_side - left_side) # abs pulls absolute diff regardless of the larger number
        differences.append(difference) # list of the differences between sections

    return min(differences) # pull lowest number from differences array

# Testing
print(f"test: [3, 1, 2, 4, 3], solution: {solution([3, 1, 2, 4, 3])}") # standard entry
print(f"test: [5, 6], solution: {solution([5, 6])}")  # minimal size
print(f"test: [1, 2, 3, 4], solution: {solution([1, 2, 3, 4])}")  # increasing sequence
print(f"test: [-3, -1, -2, -4], solution: {solution([-3, -1, -2, -4])}")  # all negative
print(f"test: [10, -5, 3, -2, 7], solution: {solution([10, -5, 3, -2, 7])}")  # mixed signs
print(f"test: [1000, 1000, 1000, 1000], solution: {solution([1000, 1000, 1000, 1000])}")  # uniform values
print(f"test: [1000, 1, 1, 1, 1], solution: {solution([1000, 1, 1, 1, 1])}")  # heavy first element
print(f"test: [5, -5, 5, -5, 5, -5], solution: {solution([5, -5, 5, -5, 5, -5])}")  # alternating signs

"""
The wording of this question made it sooo much harder than it needed to be,
but it was good practice for accumulating values from an array with iterations.
"""