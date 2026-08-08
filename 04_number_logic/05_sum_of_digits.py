#Take a number from user and find the sum of its digits

# taking an input
test_digit= int(input("enter a integer to find it's sum of digits : "))

# for operation making number positive

if test_digit < 0:
    test_digit = -test_digit

test_digit_sum = 0

while test_digit > 0:
    test_digit_sum = test_digit_sum + test_digit % 10
    test_digit = test_digit // 10

print(f"Sum of digit is : {test_digit_sum}")