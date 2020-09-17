#print we cant use as if we use print in the function rather than the return it means we are only show the output
#it does not use for further use like


def mean(mylist):
    avg = sum(mylist)/len(mylist)

    return avg


mean1 = mean([1,3,5,7,8])
print(mean1+10.1)

#it works but we print in the funcion in place of return than it doesnt work
