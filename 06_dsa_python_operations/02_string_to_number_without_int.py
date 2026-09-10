# Given: Input: "50729"
# Convert it into: 50729 without doing: int("50729")
# You must process one character at a time.

# Assuming there is a valid input string containing only digits.
def string_to_number(input_string : str) -> int:
	result=0
	
	for char in input_string:
		result=result*10+(ord(char)- ord('0'))
	
	return result

result = string_to_number("50729")
print(result)