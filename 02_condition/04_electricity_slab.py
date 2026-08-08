'''
Electricity Bill Slab

Take total units consumed.

Calculate bill using slab rates.

Example:

First 100 units
Next 100 units
Remaining units

(You may define the slab prices yourself.)
'''
# assuming no negative input

unit_consumed= float(input("Enter consumed unit : "))

first_slab_rate = 5.00
second_slab_rate = 6.00
third_slab_rate = 7.00

if unit_consumed <= 100:
    electricity_bill= unit_consumed*first_slab_rate

elif (unit_consumed <= 200):
    electricity_bill= (100*first_slab_rate)+((unit_consumed-100)*second_slab_rate)

else:
    electricity_bill= (100*first_slab_rate)+(100*second_slab_rate)+((unit_consumed-200)*third_slab_rate)

print(f"""

Slab rate per unit
**************************
First slab rate (First 100 unit) : {first_slab_rate:.2f}
Second slab rate (Next 100 unit)) : {second_slab_rate:.2f}
Third slab rate (Above 200) : {third_slab_rate:.2f}

Bill details
*************
Unit consumed : {unit_consumed:.2f}
Total Bill : {electricity_bill:.2f}

""")