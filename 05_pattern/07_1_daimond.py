# program to print pyramid equilapyrateral triangle from *

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
        print("*", end =" ")

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
        print("*", end =" ")

    #jumping to next line
    print()

