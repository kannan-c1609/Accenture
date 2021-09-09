"""
You are required to implement the following function:
	int CountKDigitNumbers(int arr[], int n, int k);
	The function accepts an array ‘arr’ of ‘n’ integers and an integer ‘k’ as its arguments. You are required to calculate the number of ‘k’ digit integers in array ‘arr’, and return the same.
	Note:
	•	n > 0
	•	k > 0
	Example:
	Input:
	arr: 1 2 22 3 34 899 112 3 44 552
	n: 10
	k: 2
	Output:
	3
	Explanation:
	2 digit integers in array ‘arr’ are {22, 34, 44}, count of them is 3, hence 3 is returned.
	Sample Input
	arr: 332 1 302 41 44 95 122 85 65 3221 775 12
	n: 12
	k: 3
	Sample Output:
	4

"""
def fun(n, a, k):
    count = 0
    for i in a:
        s = str(i)
        if(len(s) == k):
            count = count + 1
    return count

n = int(input())
a = list(map(int, input().strip().split()))[:n]
k = int(input())

print(fun(n, a, k))
