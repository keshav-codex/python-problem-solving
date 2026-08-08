'''
Match-Case Question

Restaurant Order System

Create a menu-driven restaurant ordering program using match-case.

Display the menu:

1. Burger  - ₹120
2. Pizza   - ₹250
3. Pasta   - ₹180


Take the user's choice and quantity as input.

Using match-case, calculate and display the total price.
'''
# assuming valid entry

print(f"""
To select option enter
1 => Burger  - ₹120
2 => Pizza   - ₹250
3 => Pasta   - ₹180
""")

choice= int(input("Enter your choice : "))

match choice:
    case 1:
        #Burger
        quantity= int(input("Enter Burger quantity : "))
        bill_amount = quantity*120
        print(f"""
        Bill Details
        *************
        Item : Burger
        Bill : {bill_amount}
        """)

    case 2:
            #Pizza
            quantity= int(input("Enter Pizza quantity : "))
            bill_amount = quantity*250
            print(f"""
            Bill Details
            *************
            Item : Pizza
            Bill : {bill_amount}
            """)

    case 3:
            #Pasta
            quantity= int(input("Enter Pasta quantity : "))
            bill_amount = quantity*180
            print(f"""
            Bill Details
            *************
            Item : Pasta
            Bill : {bill_amount}
            """)

    case _:
            print("Invalid Choice")

