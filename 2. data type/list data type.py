#list
# 1. basic one that we can create like this
a21 = [1,2.1,44,'kamal']
a2=[1,2,3,4];
a2 = a2.append(5)
#2. create list through range
a3 = list(range(1,100))
a4 = list(range(1,100,2))
print(a4)
#3. reverset the list
a4.reverse()
print(a4)

#indexing the list
a5 = a3[20:50]   # the indexing strat from the zreo so the commoand given it is basically the 20th index to 49
a6 = a3[10:50:2]  # in it the increment is alwys on 2

# negative indexing
a7 = a3[97:91:-1]  # it means from 97th to 91th in decreasement order
print(a7)

#how to check the attribute of any directories
# dir(list) it is the command
# for help in the attribute you can take help like   the syntex is on python console is

#help(list.append)
