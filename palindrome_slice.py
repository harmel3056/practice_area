#!/usr/bin/python3
# Uses slice method to identify whether an int or string is a palindrome 
# Returns a boolean
# Complexity is O(n), where n is the number of digits/characters


def palindrome_test(test_num):
    return str(test_num) == str(test_num)[::-1]

# Tests

print(palindrome_test(1221)) # True

print(palindrome_test(1234)) # False

print(palindrome_test("racecar")) # True

print(palindrome_test("-50005")) # False
