# Right angle traingle program print * and + simonteniously

# assuming to enter positive number for rows

rows = int(input("Enter no of rows : \n"))

# for outer rows
for i in range(1,rows+1):

    # for printing pattern
    for j in range(i):
        if i %2 != 0:
            if j %2 == 0:
                print("*", end=" ")
            else:
                print("+", end=" ")
        else:
            if j %2 == 0:
                print("+", end=" ")
            else:
                print("*", end=" ")

    #jumping on next line
    print()


    