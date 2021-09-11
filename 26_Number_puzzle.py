"""
Numbers Puzzle
	Given a set of numbers, one can arrange them in any order but must pay a penalty equal to the sum of the absolute differences between adjacent numbers.
	Return the minimum penalty that must be paid.
	Input Specification:
	input1: length of an integer array of numbers (2 <= input1 <= 1000)
	input2: integer array (1 <= input2[i] <= 10000)
	Output Specification:
	Return the minimum penalty.
	Example 1:
	input1: 3
	input2: {1, 3, 2}

"""

def sumOfMinAbsDifferences(arr, n):
    arr.sort()
    sum = 0

    sum += abs(arr[0] - arr[1]);

    sum += abs(arr[n - 1] - arr[n - 2]);

    for i in range(1, n - 1):
        sum += min(abs(arr[i] - arr[i - 1]),
                   abs(arr[i] - arr[i + 1]))

    return sum;

arr = list(map(int, input().strip().split()))
n = len(arr)
print(sumOfMinAbsDifferences(arr, n))

