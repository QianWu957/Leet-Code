
class solution:
    
    def taskArranger(self, task, weight, runtime):
        if not task or not weight or len(task) != len(weight):  # Define marginal situation
            return 0
        

        dp = [[0 for _ in range(runtime + 1)] for _ in range (len(task))]  #initialize dp 

        print(dp)

        m = len (dp) # length of task 

        n = len(dp[0]) # length of each time situation for a specific task

        #print(m)
        #print(n)

        for k in range (n):
            if 2 * task [0] <= k:
                dp [0][k] = weight[0] 

        for i in range (1,m):
            for j in range (1,n):
                if 2* task [i]:
                    dp[i][j] = max(dp[i-1][j], weight[i] + dp[i-1][j-2*task[i]]) # dp[i-1][j] 不是包括第i个工作的最大收益， 
                else:                                                         # weight[i] + dp[i-1][j-2*task[i]]weight[i] 是
                    dp [i][j] = dp[i-1][j]                                        # 包括工作i的收益 + 不包括工作i的最大收益
        return dp [-1][-1]                                                                                 

#111111111111
#2222222222
#33333333333#44444444


if __name__ == "__main__":
    task = [2,2,3,4]
    weight = [2,3,4,3]
    runtime = 9
    dp = solution()

    print(dp.taskArranger(task, weight, runtime))



