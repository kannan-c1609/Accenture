"""
Placement Season Begins
	The placement season has begun in a college. There are N number of students standing outside an interview room in a line. It is given that a person who goes in first has higher chances of getting selected.
	Each student has a number associated with them known as the problem-solving capability (PSC). The higher the capability, the higher the chances of selection. Now, each student wants to know the number of students ahead of him/her who have more problem-solving capability than him/her.
	Find this number for each student.
	Input Specification:
	input1: An integer N, which denotes the number of students present.
	input2: An array of size N, denoting the problem-solving capability of the students
	Output Specification:
	An array of size N denoting the required answer for each student.
	Example 1:
	input1: 6
	input2: {4, 9, 5, 3, 2, 10}
	Output: {0, 0, 1, 3, 4, 0}

"""
def fun(n, arr):
    #list = []
    count = 0
    print(count, end=' ')
    for i in range(1, n+1):
        count = 0
        for j in range(0, i):
            if arr[i] < arr[j]:
                count = count + 1
        #list.append(count)
        print(count, end = ' ')

n = int(input())
arr = list(map(int, input().strip().split()))[:n]
fun(n, arr)