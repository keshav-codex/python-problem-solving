#Take a number from user and check number is pelindrome or not.

# taking an input
test_digit= int(input("enter a integer to check it is pelindrom or not : "))

# for operation making number positive

if test_digit < 0:
    test_digit = -test_digit

original = test_digit
reverse_num = 0

while test_digit > 0:
    reverse_num = (reverse_num * 10) + (test_digit % 10)
    test_digit = test_digit // 10

print(f"{original} is pelindrom") if original == reverse_num else print("Not pelindrome")
