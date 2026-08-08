# program to print pyramid equilapyrateral triangle from *

# asssuming for valid input

rows= int(input("Enter number of rows : "))


print("\n Printing  pattern \n")

# outer loop for rows


for i in range(1,rows+1):
    # for inner loop and printing pattern and blank space

    # for printing blank space
    for j in range(rows-i):
        print(" ", end =" ")

    # for printing *
    for k in range(2*i-1):
        print("*", end=" ")

    # jumping to next line
    print()
