class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)

        print(dp)
        dp[0] = 1
        if len(s) == 0:
            return 0

        if s[0] == '0':
            return 0

        if s[0] != '0':
            dp[1] = 1
        else:
            0

        for i in range(1,len(s)):
            if s[i] != '0':
                dp[i+1] += dp[i]
            
            if s[i-1:i+1] <= '26' and s[i-1:i+1] >= '10':
                dp[i+1] += dp[i-1]

        return dp[-1]
