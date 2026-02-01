#!/usr/bin/python3
"""
A small frog wants to get to the other side of the road.
The frog is currently located at position X and wants to get to a
position greater than or equal to Y. The small frog always jumps
a fixed distance, D.
Count the minimal number of jumps that the small frog must perform
to reach its target.

Write a function:
    def solution(X, Y, D)
that, given three integers X, Y and D, returns the minimal number
of jumps from position X to a position equal to or greater than Y.

For example, given:
    X = 10
    Y = 85
    D = 30

the function should return 3, because the frog will be positioned as
follows:
    after the first jump, at position 10 + 30 = 40
    after the second jump, at position 10 + 30 + 30 = 70
    after the third jump, at position 10 + 30 + 30 + 30 = 100
    Write an efficient algorithm for the following assumptions:
        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.
"""
import math

"""
Notes;
X = starting point
Y = destination (equal or greater)
D = jump distance
"""
def solution(X, Y, D):
    jumps = ((Y - X) / D)
    return math.ceil(jumps) # math.ceil returns the rounded-up number of jumps

print(f"input (10, 85, 15), result {solution(10, 85, 15)}") # standard test
print(f"input (20, 20, 5), result {solution(20, 20, 5)}") # X == Y frog already at destination
print(f"input (10, 12, 30), result {solution(10, 12, 30)}") # distance smaller than D (one jump)
print(f"input (0, 100, 25), result {solution(0, 100, 25)}") # no remainder
print(f"input (1, 1000000000, 999999999), result {solution(1, 1000000000, 999999999)}") # large numbers
print(f"input (1, 50, 1), result {solution(1, 50, 1)}") # lots of jumps

"""
An alternative measure could have been to employ a manual
calculation, like so:
"""
def solution(X, Y, D):
    distance = Y - X
    return (distance + D - 1) // D
"""
This is more efficient, it avoids float, but math.ceil might
be more memorable
"""