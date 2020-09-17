# we can do this the previous program with break and continue as well
attempt = 0
while True:
    username = input("enter the password ")
    if username == "singhkamal":

        break
    else:
        attempt = attempt + 1

print("you have successfully entered and you have attempt false attempt {} times".format(attempt))

