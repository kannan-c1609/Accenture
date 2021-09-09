"""
Please do not forget to select any one language from the right, under “Select Language” drop down menu before you start coding. This is a programming question. Please write your program in the given text area. You can check your program by clicking on the “Compile” button. Once your program is finalized, you must submit your program for evaluation by clicking on the “Submit” button. Also ensure that while printing the output of your program, if required, you only print the exact output of the program, without any leading or preceding text or remark.
	Dice sum:
	Here you are given 2 unbiased dice containing 6 faces. You will be given an output sum which should be obtained by throwing two dice. You need to return the number of all possibilities where the sum on both the dice is equal to the output sum. If there are no possibilities return 0.
	Sample Input:
	10
	Output:
	3
	Explanation:
	The possible outcomes with the output sum of 10 is (5, 5), (6, 4) and (4, 6)

"""

def fun(n):
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n:
                count = count + 1
    return count

n = int(input())
print(fun(n))
