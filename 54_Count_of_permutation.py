"""
Write a program to input string and display count of all permutation of string without using any built in functions.
	Example Input:
	ABC
	Example Output:
	6
	Explanation:
	Total Permutation of the string can be: ABC ACB BAC BCA CAB CBA
	and their count is 6 which is why answer is 6

"""
def fun(n):
    size = len(n)
    fact = 1
    for i in range (1, size+1):
        fact = fact * i
    return fact

n = input()
print(fun(n))
