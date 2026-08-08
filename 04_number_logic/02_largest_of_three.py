# program to find largest from 3 input

#assuming valid input


print("Pragram started")

first_num= int(input("Enter first number"))
second_num= int(input("Enter second number"))
third_num= int(input("Enter third number"))


if first_num == second_num == third_num:
    print("all numbers are equal", first_num)

else:
    # assuming first is largest
    largest= first_num
    
    if second_num > largest:
        largest= second_num

    if third_num > largest:
        largest = third_num

    print("Largest is", largest)
