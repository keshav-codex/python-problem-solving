# write a program to check number is armstrong or not

test_num= input("enter a number to check armstrong or not : ").strip().lstrip("-")

len_test= len(test_num)

sum_test_num = 0

for digit in test_num:
    digit= int(digit)
    sum_test_num= sum_test_num + (digit ** len_test)

if sum_test_num == int(test_num):
    print(f"{test_num} is an armstrong number ")
else:
    print(f"{test_num} is not an armstrong number")
