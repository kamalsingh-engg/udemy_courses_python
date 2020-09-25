"""
the file processing is something to read ,write on other export file
qusetion 1 to read the txt file
"""

file =open("fruits.txt")
print(file.read())
print(file.read()) # it is not working because it is automatically at the lower part of the systeem
"""
file cursor :- in the last above code the file cursor is down so you can not read two time example in ablove 
so its solution is 

"""
file =open("fruits.txt")
content = file.read()
print(content)
print(content)
"""

"""