"""
Write a program that adds up the largest row sum and the largest column sum from an N – rows *M-columns array of numbers.
	As a preliminary phrase, you should reformat the sequence of numbers as a matrix, whose number of rows and columns are to be specified as arguments.
	Input Specification:
	Input1: Integer for row dimension of the array
	Input2: Integer for column dimension of the array
	Input3: Array elements to be entered in row major
	Output Specification:
	Largest row sum + Largest column sum
	Example 1:
	Input1 : 2
	Input2 : 2
	Input3: {1, 2, 5, 6}
	Output: 19
	Explanation:
	The array has 2 rows (input1) and 2 columns (inptu2). The elements in the first row are 1 and 2 and the elements in the second row are 5 and6 (input3).
	The largest sum among the two rows is 11(5 + 6). The largest sum among the two columns is 8 (2 + 6). By adding those two up, we get the final sum of 19(11 + 8).
	Example 2:
	Input1 : 3
	Input2 : 3
	Input3: {3, 6, 9, 1, 4, 7, 2, 8, 9}
	Ouput: 44
	Explanation:
	In the given matrix of 3 × 3, the row with maximum sum has a sum of 19 and the column with the maximum sum has a sum of 25, hence the total sum of the two is: 19 +25 = 44

"""

R = int(input())
C = int(input())
matrix = []

for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

rSum = 0
for i in range(R):
    Sum = 0
    for j in range(C):
        Sum = Sum + matrix[i][j]
    if rSum < Sum:
        rSum = Sum
cSum = 0
for i in range(R):
    Sum = 0
    for j in range(C):
        Sum = Sum + matrix[j][i]
    if cSum < Sum:
        cSum = Sum
print(rSum + cSum)



