#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Take the first two elements of each tuple, or use 0 for missing elements
    a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    # Return a tuple with the sum of corresponding elements
    return (a1 + b1, a2 + b2)
