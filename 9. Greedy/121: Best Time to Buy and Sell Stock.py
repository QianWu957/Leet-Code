class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        dp = [[0] * 2 for _ in range(len(prices))] 
        # print(dp)

        dp[0][0] = 0             # not holding stock
        dp[0][1] = -prices[0]      # holding stock

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]


        # l, r = 0, 1

        # maxP = 0

        # while r < len(prices):
        #     if prices[l] > prices[r]:
        #         l = r   
            
        #     else:
        #         maxP = max(maxP, prices[r]- prices[l])
        #     r+=1

        # return maxP

