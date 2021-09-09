"""
String Permutations
	You are given two strings ‘X’ and ‘Y’, each containing same no of characters.
	Write a program that can determine whether the characters of string ‘X’ can be rearranged to form the second string ‘Y’.  print  “yes” if this is possible and “no” if not.
	Input Specification:
	input1: the string ‘X’
	input2: the string ‘Y’
	Output Specification:
	Return “yes” or “no” accordingly.
	Example 1:
	input:
 zbk
	 zkb
	Output: yes
	Explanation:
	You can rearrange zbk to be zkb (by switching the characters, output is “Yes”.)
	Example 2:
Input:
sample
pleamc
	Output: no
	Explanation:
	You can not rearrange “pleam” to be “sample” ( output is “No”.)

"""
NO_OF_CHARS = 256

def String_Permutation(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    if len(str1) != len(str2):
        return 0

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0
    return 1

str1 = input()
str2 = input()
if String_Permutation(str1, str2):
    print("yes")
else:
    print("no")