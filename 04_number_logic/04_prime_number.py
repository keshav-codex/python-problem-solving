# Take a number from user and check if the number is prime

test_num = int(input("Enter a number to check: It is prime or not"))

if test_num <= 1:
    print("Not a prime number")

else:
    is_prime= True

    for i in range(2,test_num):
        if test_num % 2 == 0:
            is_prime =False
            break

    print(f"{test_num} is prime") if is_prime else print("not a prime")