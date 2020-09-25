"""
closing a file i want to say closing a file is not a  compulsary but it is use to close the file so next it is not
able to read and write
"""

file =open("fruits.txt")
print(file.read())
file.close()
print(file.read()) # it shows error because it is closed so it is not read until it is not open
