# Right angle traingle program print

# assuming to enter positive number for rows

rows = int(input("Enter no of rows : \n"))

# for outer rows
for i in range(rows,0,-1):
    
    #inner row for printing patter
    for j in range(i):
        print("*", end=" ")

    # jumping on next line
    print()