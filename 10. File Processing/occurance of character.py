"""
define a funtion in which a character and filepath is assigned by user and find out the occuranc

"""
"""
def occur(word,filepath):
    with open(filepath) as myfile:
        content = myfile.read()
        count = content.count(word)
        return count

print(occur("ok","bear.txt"))

"""
"""
write a code which collect first 90 character and write to other txt 
"""

with open("bear.txt") as myfile:
    content = myfile.read()
    content = content[: 90]

with open("bear1.txt","w") as file:
    file.write(content)