# Right angle traingle program print with numbers.

# assuming to enter positive number for rows

rows = int(input("Enter no of rows : \n"))

num_to_print=1

# for outer rows
for i in range(1,rows+1):

    #inner row for printing patter
    for j in range(i):
        print(num_to_print, end=" ")
        num_to_print +=1

    #jumping to next line
    print()