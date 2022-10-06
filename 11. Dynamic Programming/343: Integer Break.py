class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-2] * (n+1)

        print(dp)

        dp[0] = dp[1] = 0

        print(dp)

        for i in range(1,n+1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

        return dp[-1]
