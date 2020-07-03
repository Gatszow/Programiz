# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)

# We can use + operator to combine two tuples. This is called concatenation.
# We can also repeat the elements in a tuple for a given number of times using the * operator.
# Both + and * operations result in a new tuple.

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

#Advantages of Tuple over List
'''
Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

    We generally use tuples for heterogeneous (different) data types 
    and lists for homogeneous (similar) data types.
    
    Since tuples are immutable, iterating through a tuple is faster than with list. 
    So there is a slight performance boost.
    
    Tuples that contain immutable elements can be used as a key for a dictionary. 
    With lists, this is not possible.
    
    If you have data that doesn't change, implementing it as tuple will guarantee 
    that it remains write-protected.
'''