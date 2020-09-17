# in it we will format the string with multiple variable

name =input("enter your name")
father_name =input("enter your father name ")
qualification =input("enter your qualifiaction")
age = input("enter your age")
work_experience = float(input("how many year work experience"))
skill = input("skills")
salary_expectation =float(input("salary desired"))

message = "hello ,hi! my name is %s , and my father name is %s ,my qualification is %s, and i am %s year old ,i have " \
          "total %.2f year experience .and my skill is %s ,and i want %.2f package" %(name,father_name,qualification
                                                                                      ,age,work_experience,skill,
                                                                                      salary_expectation)

#print(message)

message1 = f"hello ,hi! my name is {name} , and my father name is {father_name},my qualification is {qualification}," \
          f" and i am {age} year old ,i have total {work_experience} year experience .and my skill is {skill} ," \
          f"and i want {salary_expectation} package"

print(message1)


# THERE YOU CAN SEE TWO DIFFERENT APPROACH TO PERFORM A TASK OF STRING FORMATTING WITH NUMBER OF VARIABLE