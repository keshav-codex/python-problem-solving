'''
Take a student's name, age, percentage, and passed status as input.
Print them in a neatly formatted sentence using appropriate data type conversions.
'''

# Assuming that all input is in valid type and range

print("Please enter following details\n")
name= input("Enter your name : ").strip()
age= int(input("Enter your age: "))
percentage= float(input("Enter your percentage: "))
status= input("Enter your status Passed/Failed: ").strip()


print(f"""
Hi, Student's details is :
--------------------------
    Name: {name}
    Age: {age}
    marks: {percentage}%
    Stauts: {status}
""")