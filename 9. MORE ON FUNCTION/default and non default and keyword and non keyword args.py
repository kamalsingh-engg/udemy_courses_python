"""
in it we are discussing about the different parmter of the function
"""
def area (a,b):
    area = a*b
    return area

print(area(5,4))


"""
in the above code  print(area(5,4)) the 5,4 are called non keyword parameter and we call it positional arg as well 
as we know this is not attached to the any keyword and it is directly connected to its direct posiitional

if suppose the above code print(area(a=5,b=7)) this is called keyword argument and call it non positional args as well 
as we can check 

if suppose def area (a,b=4) then b is default parameter and a is non default parameter and in it everything is working 
means all args we discuss 

but if suppose def area(a=5,b=4) then it is also applicable but def area(a=5,b) is not applicable as we know that 
default can not be pass before non default 
 """