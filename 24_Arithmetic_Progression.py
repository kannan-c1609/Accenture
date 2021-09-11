"""
Arithmetic Progression
	Given the second and the third terms of an AP(– 106<= a2, a3<= 106), find the nth (1 <= n <= 1000) term of the sequence.
	Input Specification:
	input1: Second element of series (Integer).
	input2: Third element of series (Integer).
	input3: Total number of elements in the series (Integer).
	Output Specification:
	Return the nth element of the series.
	Example 1:
	input1: 1
	input2: 2
	input3: 4
	Output: 3
	Explanation:
	a2 = 1, a3 = 2, n = 4, d = 1, an = a4 = 3(d refers to the common difference between adjacent terms in an arithmetic progression)
	Example 2:
	input1: 5
	input2: 8
	input3: 4
	Output: 11
	Explanation:
	a2 = 5, a3 = 8, n = 4, d =3, an = a4 = 11 (d refers to the common difference between adjacent terms in an arithmetic progression)

"""
def fun(a, b, n):
    d = b - a
    first = a - d
    return (first + (n-1) *d)

a = int(input())
b = int(input())
n = int(input())
print(fun(a, b, n))
