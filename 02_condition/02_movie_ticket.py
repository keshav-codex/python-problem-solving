'''
Movie Ticket Pricing

Take:

People number based on Child, Adult, Senior Citizen
Day of the week

Pricing Rules:

Child (<12): ₹120
Adult (12 - 59): ₹200
Senior Citizen (60+): ₹150
Wednesday: 20% discount
More than 5 tickets: Additional 10% discount

Print the final amount.
'''

# Assuming valid Input Data Type and range

child_count= int(input("No of children (Age < 12 ) : "))
adult_count= int(input("No of Adults (Age 12- 59) : "))
senior_count= int(input("No of Senior Citizens (Age 60 +) : "))
day= input("Enter day : ").strip()

ticket_amount= (
    (child_count*120)
    +(adult_count*200)
    +(senior_count*150)
)

total_ticket= child_count+adult_count+senior_count

if day.lower() == "wednesday":
    ticket_amount= ticket_amount*0.80

if total_ticket > 5:
    ticket_amount= ticket_amount*0.90

print(f"""
           Ticket Details
***************************************
Ticket Booked for     : {day}
total childern        : {child_count}
total adults          : {adult_count}
total senior citizens : {senior_count}
***************************************
Total ticket          : {total_ticket}
Total amount          : {ticket_amount:.2f}
***************************************
""")