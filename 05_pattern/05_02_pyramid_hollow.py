# program to print pyramid equilapyrateral triangle from *

# asssuming for valid input

rows= int(input("Enter number of rows : "))


# outer loop for rows

print("\n Printing  pattern \n")

for i in range(1,rows+1):
    # for inner loop and printing pattern and blank space

    # for printing blank space
    for j in range(rows-i):
        print(" ", end =" ")

    # for printing *
    for k in range(2*i-1):
        if (k==0 or k==(2*i-2) or i==rows):
            print("*", end=" ")
        else:
            print(" ", end=" ")


    # jumping to next line
    print()
