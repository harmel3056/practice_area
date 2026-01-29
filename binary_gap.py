#!/usr/bin/python3

"""
A binary gap within a positive integer N is any maximal sequence of consecutive 
zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of 
length 2. The number 529 has binary representation 1000010001 and contains two 
binary gaps: one of length 4 and one of length 3. The number 20 has binary 
representation 10100 and contains one binary gap of length 1. The number 15 has 
binary representation 1111 and has no binary gaps. The number 32 has binary 
representation 100000 and has no binary gaps.

Write a function:
    def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary 
representation 10000010001 and so its longest binary gap is of length 5. 
Given N = 32 the function should return 0, because N has binary representation 
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].

Notes;
- N = positive integer range of [1..2,147,483,647]
- binary gap is sequence of 0's framed by 1s
- gap can only be calculated based on binary figure (must convert)
- return 0 for no binary gaps
- return length of LONGEST binary gap only


"""

def solution(N):
    bin_str = bin(N)[2:] # bin() returns with prefix '0b', must slice to skip. Bin output is STRING

    longest = 0
    current = 0
    in_gap = False

    for char in bin_str:
        
        if char == '1':
            if in_gap: 
            # if already in a gap when 1 occurs, we update 'longest' and reset 'current'
                if current > longest:
                    longest = current
                current = 0
            
            in_gap = True # sets in_gap to True for this and all following 1s

        if char == '0' and in_gap:
            current += 1 # count zeroes when in_gap

        else:
            pass # defaults to 0 if in_gap never toggled to True

    return longest

print(bin(1)[2:], solution(1)) # 0
print(bin(3)[2:], solution(3)) # 0
print(bin(4)[2:], solution(4)) # 0
print(bin(16)[2:], solution(16)) # 0
print(bin(20)[2:], solution(20)) # 1
print(bin(529)[2:], solution(529)) # 4
print(bin(2000000000)[2:], solution(2000000000)) # 2