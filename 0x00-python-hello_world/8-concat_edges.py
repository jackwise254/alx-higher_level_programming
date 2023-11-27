#!/usr/bin/python3
str_value = "Python is an interpreted, interactive, object-oriented programming \
language that combines remarkable power with very clear syntax"
words = str_value.split()
start_index = words.index("object-oriented")
print(' '.join(words[start_index:start_index + 4] + ['with', 'Python']))
