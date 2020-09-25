with open("bear.txt") as myfile:
    content = myfile.read()
    content = content[: 90]


print(content)