'''
Input an amount in rupees.
Calculate and print how many 
₹500, ₹200, ₹100, ₹50, ₹20, ₹10, ₹5, ₹2 and ₹1 
notes/coins are required.
'''
# assuming right type input will be done

amount= int(input("Please enter an amount to calculate currency breakdown : "))

five_hundred= amount // 500
amount = amount % 500

two_hundred= amount // 200
amount = amount % 200

one_hundred= amount // 100
amount = amount % 100

fifty= amount // 50
amount = amount % 50

twenty= amount // 20
amount = amount % 20

ten= amount // 10
amount = amount % 10

five= amount // 5
amount = amount % 5

two= amount // 2
one = amount % 2

print(f"""
Currency Breakdown
***********************

₹500 : {five_hundred}
₹200 : {two_hundred}
₹100 : {one_hundred}
₹50 : {fifty}
₹20 : {twenty}
₹10 : {ten}
₹5 : {five}
₹2 : {two}
₹1 : {one}

""")