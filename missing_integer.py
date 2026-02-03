#!/usr/bin/python3

"""
Write a function:
    def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.

Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [-1,000,000..1,000,000].
"""
# 'if X not in A' inefficient, too much scanning. See solutionB
def solution(A):
    N = len(A)

    for X in range(1, N + 2):
        if X not in A:
            return X

print(f"expected: 5, actual: {solution([1, 3, 6, 4, 1, 2])}")
print(f"expected: 4, actual: {solution([1, 2, 3])}")
print(f"expected: 1, actual: {solution([-1, -3])}")
print(f"expected: 1, actual: {solution([-200, -20, 0, 20, 200])}")


# this is more efficient, uses two sets to cancel out duplicates and produce first missing int in range
# however, it assumes a permutation-like structure, so it fails when the array is in the hundreds, for instance
# we still want to check for the lowest missing number, which must be in the range of 1 to N + 1, but
# set subtraction does not guarantee the smallest missing positive.

def solutionB(A): 
    N = len(A)
    full = set(range(1, N + 2))
    partial = set(A)
    missing = full - partial

    return missing.pop() # pop returns to int

print(f"B test | expected: 5, actual: {solution([1, 3, 6, 4, 1, 2])}")
print(f"B test | expected: 1, actual: {solution([2, 2, 2, 2])}") # duplicates
print(f"B test | expected: 2, actual: {solution([1, 1, 1, 1])}") # duplicates
print(f"B test | expected: 1, actual: {solution([4, 2, 3])}") # 1 missing
print(f"B test | expected: 4, actual: {solution([1, 2, 3])}") # perfect sequence
print(f"B test | expected: 1, actual: {solution([-1, -3])}") # small test, negative numbers
print(f"B test | expected: 1, actual: {solution([-200, -20, 0, 20, 200])}") # negative and positive

# this guy successfully handles the scope of the task in an efficient manner
# switch system is the best way to verify based on values provided. It checks the array items
# are within scope and converts the false to true where relevant, then comes back to run 1 to N + 2
# until the first False is reached and that is then returned
def solutionB(A):
    N = len(A)
    present = [False] * (N + 2)  # + 2 handles the 0 for bool as well as room for N + 1

    for X in A:
        if 1 <= X <= N + 1:
            present[x] = True

    for i in range(1, N + 2):
        if not present[i]:
            return i

print(f"C test | expected: 5, actual: {solution([1, 3, 6, 4, 1, 2])}")  # mixed positives, missing in the middle
print(f"C test | expected: 1, actual: {solution([2, 2, 2, 2])}")  # duplicates, missing 1
print(f"C test | expected: 2, actual: {solution([1, 1, 1, 1])}")  # duplicates, missing 2
print(f"C test | expected: 1, actual: {solution([4, 2, 3])}")  # 1 missing, smallest case
print(f"C test | expected: 4, actual: {solution([1, 2, 3])}")  # perfect sequence, missing N+1
print(f"C test | expected: 1, actual: {solution([-1, -3])}")  # all negative
print(f"C test | expected: 1, actual: {solution([-200, -20, 0, 20, 200])}")  # negative + positive, still missing 1
