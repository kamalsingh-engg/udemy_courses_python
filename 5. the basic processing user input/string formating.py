# in it we develop a code in which user give a name and we will add hello in it

user_input = input("enter your name")
message = "hello %s" %(user_input)  # there are two different format to print message as we can see
message = f"hello {user_input}"
print(message)
