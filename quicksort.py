#!/usr/bin/python3

# Basic quicksort function

def quicksort(array):
    if len(array) < 2:  # literally just returning the one int, aka our base case
        return array
    
    pivot = array[0]    # recursive case, figures are sorted around it

    less = []
    greater = []

    for value in array[1:]:
        if value <= pivot:
            less.append(value)
        if value > pivot:
            greater.append(value)

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

"""
Notes - selecting an appropriate pivot is tres importante.

If you 'import random'
and use it as follows to generate a random pivot, it statistically gives better
partitions and avoids worst-case patterns. This is used because it turns
Quicksort into O(n log n) for all inputs.

pivot = array[random.randint(0, len(array) - 1)]

... alternatively
'Median of three' method is popular as it is cheap to compute and gives balanced
partitions. It also avoids worst case on sorted and reverse-sorted input.
first = array[0]
middle = array[len(array) // 2]
last = array[-1]

pivot = sorted([first, middle, last])[1]
"""