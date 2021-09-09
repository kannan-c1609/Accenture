"""
Write a program that takes in input as String x and returns the length of the longest palindrome subsequence of x.
	Input Specification:
	input1: string input
	Output Specification:
	Return the length of the longest palindromic subsequence.
	Example 1:
	input1: ababa
	Output: 5
	Explanation:
	Length of Longest palindromic sequence is 5 that is “ababa”
	Example 2:
	input1: umeaylnlfd
	Output: 3
	Explanation:
	Length of Longest palindromic sequence is 3 that is “lnl”.

"""

def lps(str):
    n = len(str)

    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);

    return L[0][n - 1]


n = input()
print(str(lps(n)))