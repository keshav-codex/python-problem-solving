'''
Continuous Calculator

Create a calculator that repeatedly asks for:

First number
Operator (+, -, *, /)
Second number

Perform the calculation and continue until the user chooses exit.

Handle division by zero.
'''
# Assuming valid input
print("Continuous calculator program started\n")

while True:
    first_number=int(input("Enter first number : "))
    operator=input("Enter operator + or - or * or / : ")
    second_number=int(input("Enter second number : "))

    match operator:

        case '+' :
            #addition
            print(f"""
            your desired operation {first_number} + {second_number}
            result is : {first_number + second_number}
            """)

        case '-' :
            #substraction
            print(f"""
            your desired operation {first_number} - {second_number}
            result is : {first_number - second_number}
            """)

        case '*' :
            #multiplication
            print(f"""
            your desired operation {first_number} * {second_number}
            result is : {first_number * second_number}
            """)

        case '/' :
            #divition
            if second_number == 0:
                print("Can't divide by zero\n")
                continue

            print(f"""
            your desired operation {first_number} / {second_number}
            result is : {first_number / second_number}
            """)

        case _ :
            print(f"{operator} is Invalid Operator Choice")
            continue


    choice= input("\nEnter 'no' to break or any key to continue : ").strip().lower()

    if choice == "no":
        print("\nEnding program")
        break