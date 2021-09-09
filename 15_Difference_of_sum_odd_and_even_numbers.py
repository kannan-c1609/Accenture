"""
Write a program to return the difference between the sum of odd numbers and even numbers from an array of positive integers.
	Note:You are expected to write code in the findOddEvenDifference function only which will receive the forst parameter as the number of items in the array and second parameter as array itself. You are not required to take input from the console.
	Example
	Finding the difference between the sum of odd and even numbers from a list of 5 numbers
	Input
	Input 1: 5
	Input 2: 10 11 7 12 14
	Output
	-18

"""
def Difference_of_sum_of_odd_and_even(n, a):
    odd = 0
    even = 0
    for i in a:
        if i % 2 == 0:
            even = even + i
        else:
            odd = odd + i
    return odd - even

n = int(input())
a = list(map(int, input().strip().split()))[:n]
print(Difference_of_sum_of_odd_and_even(n, a))
