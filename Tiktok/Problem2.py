class Solution:
    def coinChange(self, sizes: List[int], requirement: int) -> int:
        dp = [requirement + 1]*(requirement + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, requirement + 1):
            # 遍历背包
            for size in sizes:
                if j< size:
                    continue
                elif j >= size:
                	dp[j] = min(dp[j], dp[j - size] + 1)
                    
        if dp[requirement] < requirement+1:
            return dp[requirement]
        else:
            return -1
