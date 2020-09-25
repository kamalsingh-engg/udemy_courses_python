"""
file opening is with is a good option because we dont need to close the file and it is a good option
example
"""
with open("fruits.txt") as file:
    content = file.read()

print(content)