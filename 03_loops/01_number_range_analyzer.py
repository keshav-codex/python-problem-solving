'''
Number Range Analyzer

Take two numbers start and end.

Print:

All numbers in the range
squre of number and total sum of square
is even or odd
Sum of all numbers
Count and sum of even numbers
Count and sum of odd numbers
'''
# Assuming for integer type and valid input

print("Number Range Analyzer program")

start=int(input("Enter starting range : "))
end=int(input("Enter end range : "))

number_sum = 0
square_sum = 0
even_count = 0
even_sum = 0
odd_count = 0
odd_sum = 0

print("\nNumber range analyzer report is: ")

for i in range(start,end+1):

    print(f"""
Test number is : {i}
Squre is : {i*i}
""")
    # calculating number sum
    number_sum += i

    #calculating square sum
    square_sum += i*i

    if i % 2 == 0:
        print("This is even")
        even_count += 1
        even_sum += i

    else:
        print("This is odd\n")
        odd_count += 1
        odd_sum += i


print(f"""
**************************
    Final report
************************

sum of total number in range : {number_sum}
sum of square of all number is : {square_sum}
total even number is : {even_count}
sum of even is : {even_sum}
total odd number is : {odd_count}
sum of odd is : {odd_sum}
""")
