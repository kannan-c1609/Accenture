"""
Implement the following function:
	int MaximaOrMinima(int a, int b, int c);
	Quadratic equation: A quadratic equation is any equation having the form, ax2 + bx + c, where ‘a’ cannot be zero.
	The function accepts coefficients of a quadratic equation, ‘a’, ‘b’ and ‘c’ as its argument. Implement the function to find the maximum or minimum value of quadratic equation by substituting integer values x, where – 100 <= x <= 100. Return the values as follows:
	•	if a > 0, return the minimum value of the equation.
	•	if a < 0, return the maximum value of the equation.
	Assumption: a is not equal to zero.
	Note: Computer value lies within integer range
	Example:
	Input:
	a: 1
	b: 2
	c: 1
	Output:
	0
	Explanation:
	Since, (a > 0) output is the minimum value which is at x = – 1, output = 1 * (– 1)2 + 2 * (– 1) + 1 = 0.
	Sample Input:
	a: – 2
	b: – 8
	c: 10
	Sample Output:
	18

"""
def fun(a, b, c):
    return (a * (-1*-1)) + (b * -1) + c

a = int(input())
b = int(input())
c = int(input())

print(fun(a, b, c))
