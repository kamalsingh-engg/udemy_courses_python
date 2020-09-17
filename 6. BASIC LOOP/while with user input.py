# let we do it with user input
#example user password
attempt = 0
password = input("enter the password -->")
while password != "kamalsingh":
    password = input("enter the password again -->")
    attempt = attempt+1

print("you have successfully entered and you have attempt false attempt {} times".format(attempt))


