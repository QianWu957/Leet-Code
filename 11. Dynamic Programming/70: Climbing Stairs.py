class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1 for _ in range(n)]
        print(memo)
        memo[0] = 1 # 这里是第一级台阶
        if n> 1:
            memo[1] = 2
        for i in range(2,n): #所以第n级台阶取不到
            memo[i] = memo[i-1] + memo[i-2]

        return memo[n-1]
        
