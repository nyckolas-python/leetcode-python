class Solution(object):
    """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # My first Solution with n^2 complexity
        if len(prices) <= 1:
            return 0

        max_profit = 0
        for i in range(0, len(prices) - 1):
            if (max(prices[i+1:]) - prices[i]) > max_profit:
                max_profit = max(prices[i+1:]) - prices[i]

        return max_profit

    def maxProfit_optimized(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # The second Solution with O(n) complexity
        # Initialize the maximum profit to 0
        max_profit = 0
        # Initialize the minimum price to infinity
        min_price = float('inf')

        # Loop through the prices
        for price in prices:
            # Update the maximum profit if the current price minus the minimum price
            max_profit = max(max_profit, price - min_price)
            # Update the minimum price
            min_price = min(min_price, price)

        # Return the maximum profit achieved
        return max_profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5
    print(s.maxProfit_optimized([7,6,4,3,1])) # 0
