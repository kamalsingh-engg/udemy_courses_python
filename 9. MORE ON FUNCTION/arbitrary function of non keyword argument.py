""""
arbitrary function allowed you to pass the n number of args that is the specailities of it take an exapmle
"""

def mean(*args):
    mean1 = sum(args)/len(args)
    return mean1

print(mean(1,2,3,4,3,1,2,3))

"""
so in the case you can see i can provide n number of args but it should be non keyword or positional argumnet 

"""

"""
question:- let suppose the list is given of strings we need to write them in uppercase and sorted 
"""

def lett(*args):

    out = [out.upper() for out in args]
    return sorted(out)

print(lett("kamam","ffddf","fdfdfd","qwe","king"))