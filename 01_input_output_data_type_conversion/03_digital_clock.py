"""
Take total seconds as input and convert them into:

Hours Minutes Seconds
"""

total_seconds= int(input("Enter total seconds : "))

hours= 00
minutes = 00

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining //60
seconds = remaining % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")