# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Description: 

# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit(prices):
    profit = 0
    minPrice = prices[0]

    for i in prices:
        #print("Current Min:",minPrice)
        #print("Comparing:",minPrice,"With:",i)
        minPrice = min(minPrice, i)

        profit = max(profit, i - minPrice)

    return profit

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
#prices = [2,4,1]

max = maxProfit(prices)
print("Profit:", max)