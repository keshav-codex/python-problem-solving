# Take a number from user
# Calculate factorial of the number


test_num= int(input("Enter a number to get factorial : "))

if test_num < 0:
    print("Factorial is not defined for negative numbers : ")

else:
    factorial=1

    for i in range(1, test_num+1):
        factorial = factorial * i

    print(f"Facorial of {test_num} is : {factorial}")
