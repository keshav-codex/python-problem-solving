'''
4. Electricity Bill Summary

Take customer name, previous reading and current reading.
Calculate
Units consumed
Total bill (assume ₹7.5 per unit)
Print a formatted bill.
'''

# Assuming proper type input and current reading bigger than previous one.

customer_name = input("Enter customer name : ").strip()
previous_reading= float(input("Enter previous reading : "))
current_reading = float(input("Enter previous reading : "))

unit_consumed= (current_reading-previous_reading)
total_bill= (unit_consumed*7.5)

print(f"""
Bill Details
***********
Customer Name    : {customer_name}
Previous Reading : {previous_reading}
Current Reading  : {current_reading}
Rate             : Rs. 7.5/unit
Unit Consumed    : {unit_consumed}
Bill             : Rs {total_bill:.2f}
""")