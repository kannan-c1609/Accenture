"""
Single File Programming Question
	Write a Python program that accepts a string and calculate the number of upper case letters and lower case letters.
	Input Format:
	A string in the first line
	Output Format:
	Print the original string in the first line.
	Number of upper case characters in the second line
	Number of lower case characters in the third line
	Refer to the sample output for the exact format
	Sample testcases
	Input 1:
	The quick Brown Fox
	Output 1:
	The quick Brown Fox
	Upper case characters : 3
	Lower case characters : 13

"""
def fun(n):
    lower = 0
    upper = 0
    for i in n:
        if(i.isupper()):
            upper = upper + 1
        if(i.islower()):
            lower = lower + 1
    return upper, lower


n = input()
a , b = fun(n)
print(n)
print("Upper case characters : %d"%a)
print("Lower case characters : %d"%b)
