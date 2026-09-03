class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        min_p=max(prices)
        profit=0
        while i<len(prices):
            if prices[i]<min_p:
                min_p=prices[i]
            else:
                temp=prices[i]-min_p
                profit=temp if temp>profit else profit
            i+=1
        return profit
            


