"""
Step game:
	This is a game where there are steps numbered from 0 to the n steps. You will be on the nth step on the start of the game. Your goal to reach the 0th step at the end of the game with minimum no of jumps. If the given step’s number is even you are allowed to jump m/2 steps below at maximum and if the step no. is odd you are allowed to jump 1 step below. Now find the minimum number of steps required to win this game from the given input.
	Sample Input:
	10
	Output:
	5
	Explanation:
	10-> 5 jump – 1
	5 -> 4 jump – 2
	4 -> 2 jump – 3
	2 -> 1 jump – 4
	1 -> 0 jump – 5
	Write an algorithm to solve it.

"""
def fun(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
            count = count + 1
        else:
            n = n - 1
            count = count + 1
    return count
n = int(input())
print(fun(n))
