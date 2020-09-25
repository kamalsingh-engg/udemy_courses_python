"""
if it is with condition with the  if else then the syntex is liitle change that it what

Question :-  let suppose you have a list with the negative number which you need to  change the 0 in the list excep all
the same

"""

temps = [12,43,54,56,-98,12,-20]
temp = [temp if temp>0 else 0 for temp in temps]

print(temp)


"""
question 2:- you need to add the rows that is provided you in the list
"""
def adder(input):
    sumup = sum([(float(sumup)) for sumup in input])
    return sumup

print(adder([1,2.3,4.5,6.55,6.7,8.9,1.2,5]))
