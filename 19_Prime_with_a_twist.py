"""
Primes with a Twist
	Given an integer n (n <= n <= 104), you need to count the numbers, xi< n, which are co-prime to ‘n’, i.e. gcd(x, n) = 1.
	Formally, given n, you need to find f(n) = |{x < n : gcd(x, n) = 1}|.
	Input Specification:
	input1: the integer ‘n’
	Output Specification:
	Return the count of the number of co-primes of ‘n’.
	Example 1:
	input1: 4
	Output: 2
	Explanation:
	Integers 1 and 3 are co-prime to 4, but 2 is not.
	Example 2:
	input1: 16
	Output: 8
	Explanation:
	Integers 1, 3, 5, 7, 9, 11, 13 and 15 are co-prime to 16.

"""
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def fun(n):
    count = 0
    for i in range(1, n+1):
        if(gcd(i, n) == 1):
            count = count + 1
    return count

n = int(input())
print(fun(n))
