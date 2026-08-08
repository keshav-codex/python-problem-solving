'''
Triangle Validator

Take three sides as input.

Check:

Whether a triangle can be formed.
If yes, identify whether it is:
Equilateral
Isosceles
Scalene
'''
print("Enter length of all three side of triangle separated by space")
first,second,third= map(int,input().split())

print(f"""
********************
 Length of triangle
 *******************
First side length : {first}
Second side length : {second}
Third side length : {third}
****************************
""")

if (first+second)>third and (first+third)>second and (second+third)>first:
    if first == second == third:
        print("It's an Equilateral triangle")

    elif (first == second) or (first == third) or (third == second):
        print("It's a Isosceles triangle")

    else:
        print("It's a Scalene triangle")
else:
    print("Invalid length: Traingle can't be formed")