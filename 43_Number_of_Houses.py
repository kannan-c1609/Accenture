"""
Number of Houses
	Problem Statement
	Implement the following function:
	int NumberofHouses(int r, int unit, int arr[], int n);
	The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size n as its argument. ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ithelement of array ‘arr’ represents the amount of food present in ‘i + 1’ house number, where 0 < = i < n. Implement the function to find and return the house number, starting from 1st house (with the amount of food arr[0]), till which the amount of food is sufficient for all the rats.
	Note:
	•	Return – 1 if the array is null (or None in the case of python).
	•	Return 0 if the total amount of food from all houses is not sufficient for all the rates.
	•	Computed values lie within the integer range.
	Example:
	Input:
	r: 7
	unit: 2
	arr: 2 8 3 5 7 4 1 2
	Explanation:
	Total amount of food required for all rats = r * unit = 7 * 2 = 14. Total amount of food in 1st four houses = 2 + 8 + 3 + 5 = 18. Since, amount of food in 1st four houses is sufficient for all rats. Thus, output is 4.
	Sample Input:
	r: 4
	unit: 3
	arr: 5 6 1 5 7
	Sample Output:
	3.

"""
def fun(s, arr):
    sum = 0
    count = 0
    for i in arr:
        sum = sum + i
        count = count + 1
        if sum >= s:
            return count


n = int(input())
m = int(input())
arr = list(map(int, input().strip().split()))
print(fun(n*m, arr))