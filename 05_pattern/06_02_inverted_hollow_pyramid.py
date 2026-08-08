# program to print pyramid equilapyrateral triangle from *

# asssuming for valid input

rows= int(input("Enter number of rows : "))


print("\n Printing  pattern \n")

# outer loop for rows
for i in range(rows,0,-1):

    #printing blank spaces
    for j in range(rows-i):
        print(" ", end=" ")

    #printing *

    for k in range(2*i-1):
        if(k==0 or k==(2*i-2) or i==rows):
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    #jumping to next line
    print()