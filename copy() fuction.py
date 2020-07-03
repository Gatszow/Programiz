#The problem with copying lists in this way is that
# if you modify new_list, old_list is also modified.

old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

# However, if you need the original list unchanged when the new list is modified,
# you can use the copy() method.

# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
copied_list = my_list.copy()

# add an element to list
copied_list.append("bc")

print("\nMy list after adding \"bc\" to copied list:", my_list)
print("Copied List after adding \"bc\":", copied_list)