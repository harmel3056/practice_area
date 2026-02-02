#!/usr/bin/python3

"""
A small frog wants to get to the other side of a river. 
The frog is initially located on one bank of the river (position 0)
and wants to get to the opposite bank (position X+1). Leaves fall 
from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the
falling leaves. A[K] represents the position where one leaf falls 
at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the 
other side of the river. The frog can cross only when leaves appear 
at every position across the river from 1 to X (that is, we want to 
find the earliest moment when all the positions from 1 to X are covered
by leaves). You may assume that the speed of the current in the river 
is negligibly small, i.e. the leaves do not change their positions once
they fall in the river.

For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when
leaves appear in every position across the river.

Write a function:
    def solution(X, A):

that, given a non-empty array A consisting of N integers and integer X,
returns the earliest time when the frog can jump to the other side of the
river.

If the frog is never able to jump to the other side of the river, the
function should return −1.

For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""
# essentially wants a full set from 1 to X
# if you store values in a set (which doesn't accept diplicates) then logically you
# just need to ensure X number of leaves are attained, as X unique numbers

def solution(X, A):
    seen = set() # sets don't allow duplicates, so it quickly removes those. stores all unique positions.
    needed = X # starting point is number needed to get to other side

    for time, position in enumerate(A): # loops over the array and returns both the index and the value

        if position not in seen:
            seen.add(position) # .add is the set() equiv of .append for list/array
            needed -= 1

            if needed == 0: # required leaves has been reached
                return time # time ticks through as you loop through position. Returning the index(time)

    return -1 # fallback if crossing unachievable

print(f"X=5, A=[1,3,1,4,2,3,5,4], solution: {solution(5, [1,3,1,4,2,3,5,4])}")  # expect 6
print(f"X=1, A=[1], solution: {solution(1, [1])}")  # expect 0
print(f"X=3, A=[1,1,1], solution: {solution(3, [1,1,1])}")  # expect -1