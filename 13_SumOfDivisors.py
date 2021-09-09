"""
Sum of Divisors
	Given an integer ‘n’ (1 <= n <= 109), find the sum of its unique divisors.
	Input Specification:
	Input 1: the integer ‘n’
	Output Specification:
	Return the sum of divisors of ‘n’.
	Example 1:
	Input 1: 6
	Output: 12
	Explanation:
	Divisors of 6 are 1, 2, 3 and 6. Sum od number (i.e 1 + 2 + 3 + 6) is 12
	Example 2:
	Input1: 36
	Output: 91

"""

def sumOfDivisors(n):
    sum = 0
    for i in range(1, n+1):
        if(n % i == 0):
            sum = sum + i
    return sum


n = int(input())
print(sumOfDivisors(n))
