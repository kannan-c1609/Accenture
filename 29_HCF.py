"""
Highest Common Factor
	Find the HCF (Highest Common Factor) of n numbers given in an integer array. Fill in the function HCF() and return the HCF.
	Input Specification:
	input1: the size array
	input2: an integer array
	Output Specification:
	Return the HCF of given numbers
	Example 1:
	input 1:3
	input 2: {2, 4, 8}
	Output: 2
	Explanation:
	The common factor for 2, 4, 8 are 1 and 2. Hence the HCF(Highest Common Factor) is 2.
	Example 2:
	input1: 5
	input2: {10, 15, 20, 35, 70}
	Output: 5

"""
def findGCD(a, b):
    while(b):
        a, b = b, a % b
    return a

def fun(a, n):
    result = a[0]
    for i in range(1, n):
        result = findGCD(a[i], result)
    return result

n = int(input())
a = list(map(int, input().strip().split()))[:n]
print(fun(a, n))