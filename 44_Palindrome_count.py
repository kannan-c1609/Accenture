"""
Palindrome Count
	Write a function to find all the words in a string which are palindrome.
	Note: A string is said to be a palindrome if the reverse of the string is the same as string. For example, “abba” is a palindrome, but “abbc” is not a palindrome.
	Input Specification:
	Input1: string
	Input2: Length of the String
	Output Specification:
	Return the number of palindromes in the given string
	Example 1:
	Input1: this is level 71
	Input2: 16
	Output: 1
	Explanation:
	The reverse of the word “level” is “level”. Hence, the word is a palindrome. As the string contains only one palindrome, so the returned value will be 1.
	Example 2:
	Input1: hello world
	Input2: 11
	Output: 0
	Explanation:
	As the given string doesn’t contain any palindrome, so the returned value will be 0.

"""

def fun(n):
    a = n.split(' ')
    count = 0
    for i in a:
        if i ==  i[::-1]:
            count = count + 1
    return count

n = input()
size = int(input())
print(fun(n))
