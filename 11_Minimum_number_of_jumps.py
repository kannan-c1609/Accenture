"""
Minimum Number of Jumps
	Given an array of integers, where each element represents the maximum number of jumps that can be taken forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element).
	It an element is 0, then no jump can be made from that element. If it is not possible to reach the end, then output –1.
	Input Specification:
	Input1: number of elements in array input2. (2 <= input1 <= 1000)
	Input2: an integer array
	Output Specification:
	Return the minimum number of jumps to reach the end.
	Example 1:
	Input1 : 3
	Input2: {2, 1, 1}
	Output: 1
	Explanation:
	The first element is 2, this means that 2 jumps can be taken forward from this element. With this, we reach the last element. Hence, the total number of required jumps is 1.
	Example 2:
	Input1: 9
	Input2: {1, 3, 6, 1, 0, 9, 8, 7, 6}
	Output: 3
	Explanation:
	The first element is 1, this means that 1 jump can be taken and reach element 3. Now, 3 jumps can be taken forward from this element. On taking the first step, we get element 6. If 6 jumps are taken from here itself, the last element of the array will be reached. Hence, the total number of required jumps will be 3.

"""


def minJumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


n = int(input())
arr = list(map(int, input().strip().split()))[:n]

print(minJumps(arr, n))