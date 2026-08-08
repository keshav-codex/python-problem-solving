'''
TM Cash Withdrawal

Take the following inputs:

Account Balance
Withdrawal Amount

Check:

Amount should be a multiple of 100.
Balance should be sufficient.
Minimum balance after withdrawal should remain ₹1000.

Display the appropriate message.
'''
# Assuming for entering right value

account_balance= float(input("Enter account balance : "))
withdraw_amount= int(input("Enter ammount to withdraw : "))

if (account_balance < 0 ):
    print("Amount can't be negative")

elif (withdraw_amount % 100 != 0):
    print("Withdrawal amount must be multiple of 100")

elif (account_balance < withdraw_amount):
    print("Insufficient Amount")

elif account_balance - withdraw_amount < 1000:
    print("Minimum balance of ₹1000 must be maintained.")

else:
    print(f"""
    Transaction successfull
    Withdrawal ammount : {withdraw_amount :.2f}
    Balance ammount : {account_balance - withdraw_amount :.2f}
    """)