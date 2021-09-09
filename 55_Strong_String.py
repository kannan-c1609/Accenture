"""
Write a program to take string as input and check if it contains only character or not, numeric and special symbols are not allowed. After that, reverse that string without using built in functions. If entered and reverse string both are same than give message as provided in double quotes “you inputted a strong string”, otherwise print “you inputted it weak string.”
	Example Input:
	wowu
	Example Output:
	you inputted a weak string
	Example Input:
	wow
	Example Output:
	you inputted a strong string.

"""
def fun(n):
    flag = 1
    for i in n:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            flag = 0
        else:
            flag = 1
            return flag
    size = len(n)
    i = 0
    j = size - 1
    while i < size // 2:
        if(n[i] != n[j]):
            return 1
        i = i + 1
        j = j - 1
    return 0

n = input()
result = fun(n)
if result == 1:
    print("you inputted a weak string")
else:
    print("you inputted a strong string")