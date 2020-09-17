#with the dictionary the three things is very important

#items:- it complete get from the dictionary
#keys :- it is the the main keyword which is probably string
#values :- it is the relative value in compare to it


dict = {"monaday":22.3,"tuesday":24,"wednesday":26,"thursday":30,"friday":29,"saturday":28,"sunday":27}

for item in dict.items():
    print(item)

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

#this is the different ways to use for loop with dictionary

#one more example with it

dict = {"monaday":22.3,"tuesday":24,"wednesday":26,"thursday":30,"friday":29,"saturday":28,"sunday":27}

for temp in dict.items():
    print("the temp of %s is %.2f" %(temp[0],temp[1]))

#in other ways

for key,value in dict.items():
    print("the temp of {} is {}" .format(key,value))


