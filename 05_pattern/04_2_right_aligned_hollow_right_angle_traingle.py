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
        if (k==0 or k+1==i or i==rows):
            print("*", end=" ")
        else:
            print(" ", end=" ")


    # jumping to next line
    print()

