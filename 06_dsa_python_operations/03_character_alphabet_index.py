'''
Given: s = "leetcode"

Convert every character into its zero-based alphabet index:

l → 11  e → 4    e → 4   t → 19     c → 2   o → 14  d → 3   e → 4

Output: [11, 4, 4, 19, 2, 14, 3, 4]

Then reverse the operation:

11 → l  4  → e  19 → t  using chr().
'''

def char_index(input_string : str) -> None:
	
	result=[]
	
	for char in input_string:
		if char.isalpha():
			result.append(ord(char.lower())-ord('a'))
	
	print(result)
	
	# Reverse the operation

	for i in result:
		print(i ," : ", chr(i+ord('a')))

if __name__ == "__main__":
	char_index("leetcode")