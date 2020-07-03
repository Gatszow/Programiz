from fractions import Fraction as F

# Output: 3/2
print(F(1.5))

# Output: 5
print(F(5))

# Output: 1/3
print(F(1,3))

# FLOATS

# As float
# Output: 2476979795053773/2251799813685248
print(F(1.1))

# As string
# Output: 11/10
print(F('1.1'))

# Basic Operations:

print(F(1, 3) + F(1, 3))

print(1 / F(5, 6))

print(F(-3, 10) > 0)

print(F(-3, 10) < 0)