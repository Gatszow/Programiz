import os

# Pokazanie teraźniejszego źródłą
print(os.getcwd())

# Zmiana źródła
'''
os.chdir("C:\\Users\\Takezaki\\PycharmProjects")

print(os.getcwd())

os.chdir("C:\\Users\\Takezaki\\PycharmProjects\\Programiz")

print(os.getcwd())
'''


# Pokazanie listy plików
'''
print(os.listdir("C:\\"))
'''


# Stworzenie nowego folderu
'''
os.mkdir("Test")
'''

# Zmiana nazwy folderu
'''
os.rename("Test", "Nowy")
'''

# Usunięcie pliku tekstowego, obrazkowego itp/
"""
os.remove("Lola")
"""

print(os.listdir())

# Usunięcie pustego folderu
'''
os.rmdir("Nowy")
'''

# Usunięcie folderu z plikami
'''
import shutil

shutil.rmtree('Shutil')
'''