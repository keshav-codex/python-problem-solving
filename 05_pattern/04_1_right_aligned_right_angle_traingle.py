# program to print equilateral triangle from *


# asssuming for valid input

rows= int(input("Enter number of rows : "))


# first version 
# outer loop for rows

print("\n Printing first version\n")

for i in range(1,rows+1):
    # for inner loop and printing pattern and blank space

    # for printing blank space
    for j in range(rows-i):
        print(" ", end =" ")

    # for printing *
    for k in range(i):
        print("*", end=" ")

    # jumping to next line
    print()



# second version
# outer loop for rows

print("\n Printing second version\n")

for i in range(rows,0,-1):
    # for inner loop and printing pattern and blank space

    # for printing blank space
    for j in range(i-1):
        print(" ", end =" ")

    # for printing *
    for k in range(rows-i+1):
        print("*", end=" ")

    # jumping to next line
    print()
