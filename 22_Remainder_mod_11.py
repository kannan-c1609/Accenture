"""
Remainder mod 11
	Given a string (of maximum length 1000) representing a large number, output its remainder modulo 11.
	Input Specification:
	Input1: a large number in the form of a string.
	Output Specification:
	Return the remainder modulo 11 of input1.
	Example 1:
	input1: 121
	Output: 0
	Explanation:
	121 mod 11 = 0
	Example 2:
	input1: 452
	Output: 1
	Explanation:
	452 mod 11 = 1

"""

def remainder(st):
    ln = len(st)

    rem = 0

    for i in range(0, ln):
        num = rem * 10 + (int)(st[i])
        rem = num % 11

    return rem

st = input()
print(remainder(st))