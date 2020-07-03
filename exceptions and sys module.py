import sys

# Wersja używająca modułu sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)



# Wersja nieużywająca modułu sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r, end="\n\n")



# Najlepiej oznaczać co program ma zrobić przy danym wyjątku
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass



# Samodzielne uaktywnianie wyjątku
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)


#Python try...finally
'''
The try statement in Python can have an optional finally clause. 
This clause is executed no matter what, and is generally used to release external resources.

For example, we may be connected to a remote data center through the network 
or working with a file or a Graphical User Interface (GUI).

In all these circumstances, we must clean up the resource before the program comes to a halt 
whether it successfully ran or not. These actions (closing a file, GUI or disconnecting from network) 
are performed in the finally clause to guarantee the execution.
'''
# Here is an example of file operations to illustrate this.
'''
try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
'''

