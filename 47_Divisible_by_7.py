"""
Write a Program TO find SUM of ALL integers BETWEEN two integer numbers taken as input AND are divisible BY 7.
	Constraint:
	Input1 < Input2
	Example Input:
	1
	20
	Example Output:
	21

"""
def fun(a, b):
    sum = 0
    for i in range(1, b+1):
        if i % 7 == 0:
            sum = sum + i
    return sum

a = int(input())
b = int(input())
print(fun(a, b))
