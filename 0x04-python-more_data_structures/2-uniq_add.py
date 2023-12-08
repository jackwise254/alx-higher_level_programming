#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()
    # Iterate through the elements in the list
    for num in my_list:
        # Add the integer to the set
        unique_integers.add(num)
    # Return the sum of unique integers
    return sum(unique_integers)
