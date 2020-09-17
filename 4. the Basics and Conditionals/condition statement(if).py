# if is use for the condition so now we are using it with the function

# like in the previous example as we  find the avg of list if suppose dictionary is given then we need to use the
# condition here
""""
def mean(value):
    if type(value) == dict:

        avg = sum(value.values())/len(value)

    else:
        avg = sum(value)/ len(value)

    return avg


mean1 = [1,2,3,4,5,33,22,12]
mean2 = {"kamal":11,"mohit":34,"fgrfr":76,"sdsds":23}
print(mean(mean2))

"""
# the above code can be written as in case is instance
def mean(value):
    if isinstance(value,dict):

        avg = sum(value.values())/len(value)

    else:
        avg = sum(value)/ len(value)

    return avg


mean1 = [1,2,3,4,5,33,22,12]
mean2 = {"kamal":11,"mohit":34,"fgrfr":76,"sdsds":23}
print(mean(mean2))

#elif function

def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"

print(foo(16))