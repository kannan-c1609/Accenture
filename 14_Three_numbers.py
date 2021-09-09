"""
Given three numbers b, e, and m. Fill in a function that takes these three positive integer values and outputs be mod m.
	Note: The test case values can be very large. Therefore, write your code accordingly.
	Input Specification:
	Input 1: positive integer, b
	Input 2: positive integer, e
	Input 3: positive integer, m
	Output Specification:
	Return an integer on calculating be mod m.
	Example 1:
	Input 1: 2
	Input 2: 10
	Input 3: 1025
	Output: 1024

"""

def Three_numbers(b, e, m):
    return (b ** e) % m

b = int(input())
e = int(input())
m = int(input())

print(Three_numbers(b, e, m))
