""""
here we can apply if condition also with the list in order to control and modification in the list
here we are using the syntex due to which we does not need to append the list

"""
temps = [12,43,54,56,-98,12,-20]
temp = [temp/10 for temp in temps if temp>0]

print(temp)

"""
only integer number need to show 

"""
def list1(input1):
    temp1 =[]
    temp1 = [temp1 for temp1 in input1 if isinstance(temp1,int)]
    return temp1

print(list1([12,34,45,-23,"kmal","qwe",34.5]))

#this is basically when we use the list with the if condition
