'''
Given two non-negative integer strings:
num1 = "50729"
num2 = "6843"
Calculate their sum without using:
int()
float()
eval()
+ on the complete numbers
Python's built-in arithmetic conversion
You must process one digit at a time.
'''


def add_strings(num1: str, num2: str) -> None:
	
    result =[]
    carry= 0

    n1 = len(num1)-1
    n2 = len(num2)-1

    while n1 >= 0 or n2 >= 0 or carry:
        if n1 >= 0:
            digit1 = ord(num1[n1]) - ord('0')
        else:
            digit1 = 0

        if n2 >= 0:
            digit2 = ord(num2[n2]) - ord('0')
        else:
            digit2 = 0

        sum = digit1 + digit2 + carry

        result.append(str(sum % 10))
        carry = sum // 10

        n1 -= 1
        n2 -= 1

    print(''.join(result[::-1]).lstrip('0') or '0')

if __name__ == "__main__":
    add_strings("50729", "6843")