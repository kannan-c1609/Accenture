"""
You are required to implement the following function:
	int MatchString(char str1[], int len1, char str2[], int len2, int k1, int k2);
	The function accepts two strings ‘str1’ and ‘str2’ of length ‘len1’ and ‘len2’ respectively and two integers ‘k1’ and ‘k2’ as its arguments. Implement the function to compare each index of ‘str1’ and ‘str2’ leaving out the first ‘k1’ characters from ‘str1’ and ‘k2’ characters from ‘str2’ respectively till the end of each string and return an integer as per the following rules in the given priority:
	1.	If all the remaining characters match, then return the length of the match
	2.	Return 0, if remaining characters to be matched for either of the string is 0 or both the strings are null (or None in case of python)
	3.	Return -1, in case of mismatch in characters or count of remaining characters or one of the string, is null (or None in case of python)
	Assumption:
	•	‘str1’ and ‘str2’ contain lower case alphabets only
	•	Index starts from 0
	•	0 <= k1 <= len1
	•	0 <= k2 <= len2
	Example:
	Input:
	k1: 4
	k2: 7
	str1: succeed
	str2: crossbreed
	Output:
	3
	Explanation:
	Leaving first the 4 characters in ‘succeed’, string left is ‘eed’, similarly after leaving first the 7 characters in ‘crossbreed’, string left is ‘eed’
	Since all the remaining characters match and the length of the match is 3, hence the output is 3.
	Sample Input:
	k1: 5
	k2: 5
	str1: remember
	str2: customer
	Sample Output
	– 1

"""

def fun(m, n, a, b):
    str1 = a[m:]
    str2 = b[n:]
    if len(str1) == 0 or len(str2) == 0:
        return 0
    if str1 == str2:
        return len(str1)
    else:
        return -1

m = int(input())
n = int(input())
a = input()
b = input()

print(fun(m, n, a, b))