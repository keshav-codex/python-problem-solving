'''
Take input separately as

day
month
year

Print

DD/MM/YYYY  =>    05/08/2026
DD-MMM-YYYY  =>   05-Aug-2026
Month DD, YYYY   =>   August 05, 2026

(No datetime module.)
'''
# assuming for right input

day= int(input("Enter day like (01-31) : "))
month_number= int(input("Enter months (01-12) : "))
year= int(input("Enter Year like 2026 : "))

months_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month = months_list[month_number-1]

print(f"{day:02}/{month_number:02}/{year}")
print(f"{day:02}-{month[:3]}-{year}")
print(f"{month} {day:02},{year}")
