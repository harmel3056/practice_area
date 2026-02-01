#!/usr/bin/python3

"""
Write a function that prints the numbers from 1 to 100.
But for multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz".
For numbers that are multiples of both 3 and 5, print "FizzBuzz".
"""

def FizzBuzz():
    x = 1 # starting point

    for n in range(1, 101)
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0: # elif not if to ensure no double-down
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else: print(x) # fallback to standard ints

        x += 1
    return

print(FizzBuzz())
