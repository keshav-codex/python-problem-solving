'''
Digit Analyzer

Take an integer and analyze its digits using a loop.

Display:

Number of digits
Sum of digits
Even digits count
Odd digits count
Largest digit
'''
# asssuming valid input

test_integer= input("Enter an integer for digit operation : ").lstrip("-")

digit_count= digit_sum= even_digit_count = odd_digit_count = 0
largest_digit = int(test_integer[0])

for digit in test_integer:

    digit = int(digit)

    digit_count += 1
    digit_sum += digit

    if digit %2 == 0:
        even_digit_count += 1
    else:
        odd_digit_count += 1

    if digit > largest_digit:
        largest_digit = digit

print(f"""
In provided integer
digit count : {digit_count}
sum of digit : {digit_sum}
even digit : {even_digit_count}
odd digit : {odd_digit_count}
largest digit : {largest_digit}

""")