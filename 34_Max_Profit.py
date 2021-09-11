"""
Implement the following function:
	int MaxProfit(int* price, int n);
	The function accepts a positive integer array ‘price’ consisting of ‘n’ elements as its argument. ‘price’ contains prices of a share throughout the day in the order of their occurrence. When a new price occurs, old price disappears forever. A transaction for the share is complete when firstly the share is bought and the sold. In a transaction where the share is bought at price[j] and sold at price[k], where j < k, profit for that transaction = price[k] – price[j]. You can use a price only once either to buy or sell the share. Implement the function to maximize the profit in at most 2 transactions and return the same. Transaction 2 starts only when transaction 1 is completed.
	Note:
	•	If ‘price’ is empty or None in case of Python, return -1.
	•	Return 0, if n < 2.
	•	All calculations lie within integer range.
	Example:
	Input:
	price: 2 30 15 10 8 25 80
	Output:
	100
	Explanation:
	•	For Transaction 1, share is bought at 2 and sold at 30. Profit = 30 – 2 = 28.
	•	For Transaction 2, share is bought at 8 and sold at 80. Profit = 80 – 8 = 72.
	•	Total profit = Transaction 1 profit + Transaction 2 profit = 28 + 72 = 100.
	Thus, output is 100.
	Sample Input:
	price: 10 5 22 65 8 75 90 80
	Sample Output:
	142

"""

def findMaxProfit(price):

	profit = 0

	j = 0
	for i in range(1, len(price)):
		if price[i - 1] > price[i]:
			j = i

		if price[i - 1] <= price[i] and \
				(i + 1 == len(price) or price[i] > price[i + 1]):
			profit += (price[i] - price[j])

	return profit

if __name__ == '__main__':

    n = int(input())
    price = list(map(int, input().strip().split()))[:n]
    print(findMaxProfit(price))
