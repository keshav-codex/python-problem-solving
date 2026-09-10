'''
Given: s = "leetcode"

Count the frequency of every character into its zero-based alphabet index:
'''

def char_frequency(input_string : str) -> None:
	
	result=[0] * 26
	
	for char in input_string:
		if char.isalpha():
			result[(ord(char.lower())-ord('a'))] +=1
	
	print(result)
	
	print("Albhabet : Count")
	for i in range(25):
		if result[i] != 0:
			print(chr(i+97) + " : " + str(result[i]))

if __name__ == "__main__":
	char_frequency("leetcode")
