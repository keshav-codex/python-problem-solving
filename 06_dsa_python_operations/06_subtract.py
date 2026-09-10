'''
Given two non-negative integer strings:
num1 = "50729"
num2 = "6843"
Calculate their difference without using:
int()
float()
eval()
- on the complete numbers
Python's built-in arithmetic conversion
You must process one digit at a time.
'''

def subtract_strings(num1: str, num2: str) -> None:
   
    result =[]
    borrow = False
    negative_result = False

    if is_smaller(num1, num2):
        negative_result = True
        num1, num2 = num2, num1

    n1 = len(num1)-1
    n2 = len(num2)-1

    while n1 >= 0 or n2 >= 0:

        if n1 >= 0:
            digit1 = ord(num1[n1]) - ord('0')
        else:
            digit1 = 0

        if borrow:
            digit1 -= 1
            borrow = False

        if n2 >= 0:
            digit2 = ord(num2[n2]) - ord('0')
        else:
            digit2 = 0

        if digit1 < digit2:
            digit1 += 10
            borrow = True

        diff = digit1 - digit2

        result.append(str(diff % 10))

        n1 -= 1
        n2 -= 1
 
    result = ''.join(result[::-1]).lstrip('0') or '0'

    if negative_result and result != '0':
        result = '-' + result

    print(result)


def is_smaller(num1: str, num2: str) -> bool:

    if len(num1) < len(num2):
        return True

    if len(num1) > len(num2):
        return False

    for i in range(len(num1)):

        if num1[i] < num2[i]:
            return True

        if num1[i] > num2[i]:
            return False

    return False

if __name__ == "__main__":
    subtract_strings("100", "105")