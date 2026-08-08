'''
Multiplication Table Range

Take a number n and print its multiplication table from 1 to 10.

Then ask for another number and print its table and sum of all.

Continue until the user chooses to stop.
'''
#Assuming valid input

print("multiplication table range program\n")


while True:
    test_num = int(input("Enter a number to get table : "))
    table_sum =0

    print(f"\nNumber is: {test_num}")
    
    # printing table and addind sum
    for i in range(1,11):
        print(f"{test_num} * {i} = {test_num*i}")
        table_sum += test_num*i

    # printing sum
    print(f"Total sum of table is : {table_sum}")

    #asking for more numbers
    choice = input("Enter 'no' to stop program ").strip().lower()

    #checking choise for stopping
    if choice == "no":
        print("Stopping program")
        break