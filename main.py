import constants as const

print(const.PI)

print("{} is {} number?".format(const.PI,"float"), isinstance(const.PI, float))
print("{} is {} number?".format(1+2j, "complex"), isinstance(1+2j, complex))



digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

def function(args):
    pass

class Example:
    pass



def greet(name):
    """
This function greets to
the person passed in as
a parameter
    """
    print("Hello, " + name + ". Good morning!")

print(greet.__doc__)


# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))


# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

'''If we change the value of a nonlocal variable, 
the changes appear in the local variable. '''


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

