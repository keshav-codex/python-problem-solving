# write a program to print fabonacci series

# assuming valid input

test_num= int(input("Enter a number to get fabonacci series : "))

if test_num < 0:
    print("Enter a non negative number")

else:
    pre = 0
    post = 1

    print("Printing fabonacci series")

    # genrating series

    for i in range(test_num):
        print(pre, end=" " )
        next_num = pre + post
        pre = post
        post = next_num
