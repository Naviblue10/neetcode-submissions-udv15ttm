class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_in_hand=False
        total_profit=0
        for i,a in enumerate(prices):
            if i<len(prices)-1:
                if not stock_in_hand and prices[i]<prices[i+1]:
                    stock_in_hand=True
                    buy=a
                elif stock_in_hand and prices[i]>prices[i+1]:
                    sell=a
                    total_profit+=(sell-buy)
                    stock_in_hand=False
            elif stock_in_hand:
                sell=a
                total_profit+=(sell-buy)
                
        return total_profit

