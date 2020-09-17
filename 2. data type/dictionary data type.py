#dictionary always created with curly bracket
#which has two main ingredient one is keys and other is values so lets calculated the  avg. of the student

student_grades ={"kamal":9.0,"rohit":8.0,"mohan":7.5,"lakhan":8.2}
sum1 = sum(student_grades.values())
length =len(student_grades)

avg = sum1/length
print(avg)
print(student_grades.keys())