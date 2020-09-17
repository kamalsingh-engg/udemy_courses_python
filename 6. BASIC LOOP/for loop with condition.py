# for can be used with the condition

#excercise
# suppose you have a list of temp of ranging 20 to 50 you need to create the list which having only the temp below
# 40 from this list

list =[25,34,45,22,46,34,45,23,36,38]
list1 =[];

for i in list:
    if i<40:
        list1.append(i)

print(list1)

#excercise

# if we have the list of string ,float, int all so we need to  create a list which contain only float

list2 = ["kamal",23.45,56,55.4,67,12,23,45.7,32.2,78.5,6.4,22,"singh"]
list3 =[];
for j in list2:
    if isinstance(j,float):
        list3.append(j)


print(list3)
