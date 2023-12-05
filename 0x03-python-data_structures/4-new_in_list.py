def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list
    
    # Create a copy of the original list and modify the element at the specified index
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

