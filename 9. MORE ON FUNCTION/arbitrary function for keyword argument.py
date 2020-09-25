"""
this is the function in which we can define the n number of keword args
example
"""

def mean(**kwargs):
    out = sum(kwargs.values())/len(kwargs.values())
    return out

print(mean(x=1,y=3,z=5))