"""
Write a program to take two integers m & n as input and find the number of possible sequences of length n such that each of the next elements is greater than or equal to twice of the previous element but less than or equal to m.
	Example 1:
	Input:
	10
	4
	Output: 4
	Explanation: There should be n elements and value of last element should be at-most m.
	The sequences are {1, 2, 4, 8} {1, 2, 4, 9}, {1, 2, 4, 10}, {1, 2, 5, 10}.
	Example 2:
	Input:
	5
	2
	Output: 6
	Explanation: The sequences are {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}.
	Expected Time Complexity: O(m*n)
	Expected Auxiliary Space: O(1)
	Constraints: 1 ≤ m, n ≤ 100

"""
def getTotalNumberOfSequences(m, n):
    if m < n:
        return 0

    if n == 0:
        return 1

    res = (getTotalNumberOfSequences(m - 1, n) +
           getTotalNumberOfSequences(m // 2, n - 1))
    return res

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    print(getTotalNumberOfSequences(m, n))
