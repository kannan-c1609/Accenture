"""
Create a program that take a name as input and returns a greeting.
	Examples Input:
	Gerald
	Example Output:
	Hello Gerald!
	Examples Input:
	Tiffany
	Example Output:
	Hello Tiffany!

"""
def Greeting(n):
    return 'Hello ' + n + '!'

n = input()
print(Greeting(n))
