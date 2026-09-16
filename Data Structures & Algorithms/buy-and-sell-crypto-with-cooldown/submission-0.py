class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0

        if len(prices)<=1:
            return 0

        for price in prices:
            new_hold = max(hold, rest-price)
            new_sold = hold+price
            new_rest = max(rest, sold)

            hold = new_hold
            sold = new_sold
            rest = new_rest

        return max(sold, rest)