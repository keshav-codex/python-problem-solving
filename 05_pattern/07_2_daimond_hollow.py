# program to print pyramid equilapyrateral triangle from * only on border

# asssuming for valid input

rows= int(input("Enter number of rows : "))


print("\n Printing  pattern \n")

#printing upper part

    # outer loop for rows

for i in range(1,rows+1):

    # inner lopp for printing pattern

    # printing blank
    for j in range(rows-i):
        print(" ", end =" ")

    # printing *

    for k in range(2*i-1):
        if (k==0 or k==(2*i-2)):
            print("*", end =" ")
        else:
            print(" ", end=" ")

    #jumping to next line
    print()


# printing lower part
    
    # outer loop for rows

for i in range(rows-1,0,-1):

    # inner lopp for printing pattern
    
    # printing blank
    for j in range(rows-i):
        print(" ", end =" ")

    # printing *

    for k in range(2*i-1):
        if (k==0 or k==(2*i-2)):
            print("*", end =" ")
        else:
            print(" ", end=" ")
        

    #jumping to next line
    print()