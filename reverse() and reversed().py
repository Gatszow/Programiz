
# If you want to reverse your list, use reverse() function

# Operating System List
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# List Reverse
systems.reverse()

# updated list
print('Updated List:', systems)



#But if you need to access individual elements of a list in the reverse order,
# it's better to use reversed() function.

# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)