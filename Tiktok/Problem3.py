class Solution:
    def ways(self, forest: List[str], number: int) -> int:
        row, col = len(forest), len(forest[0])
        preSum = [[0 for _ in range(col)] for _ in range(row)]#存放以（i,j）为左上角，（row-1,col-1）为右下角的矩形块中的苹果数
        dp = [[[-1 for _ in range(number+1)] for _ in range(col) ]for _ in range(row)] 

        for i in range(row-1,-1,-1): #使用动态规划，二维前缀和完成这个过程
            for j in range(col-1,-1,-1):
                if i == row-1 and j == col-1:
                    if forest[i][j] == 'A':
                        preSum[i][j] = 1
                    else:
                        0
                else:
                    if i == row-1:
                        preSum[i][j] = preSum[i][j+1] + 1 if forest[i][j] == 'A' else preSum[i][j+1]
                    
                    elif j == col-1:
                    
                        preSum[i][j] = preSum[i+1][j] + 1 if forest[i][j] == 'A' else preSum[i+1][j]
                    else:
                        preSum[i][j] = preSum[i+1][j] + preSum[i][j+1] - preSum[i+1][j+1]
                        if forest[i][j] == 'A':
                            preSum[i][j] += 1
                        else:
                            0

        def dfs(x,y,num):
            tree = preSum[x][y] #以（x,y）为左上角的矩形的苹果数
            if tree < num: #苹果数不够，返回0
                return 0

            if dp[x][y][num] != -1: #备忘录，如果之前计算过，直接返回
                return dp[x][y][num]
            
            if num == 1: #分成一块，不需要切，直接返回1
                return 1

            dp[x][y][num] = 0 #计算
            
            for i in range(x+1,row): #横向切
                if preSum[i][y] < tree: #切下来的有苹果才行
                    tem = dp[x][y][num] + dfs(i,y,num-1)
                    dp[x][y][num] = tem
                    # dp[x][y][num] += dfs(i,y,num-1) #dfs
            for i in range(y+1,col): #竖着切
                if preSum[x][i] < tree: #切下来的有苹果才行
                    tem = dp[x][y][num] + dfs(x,i,num-1)
                    dp[x][y][num] = tem
                    # dp[x][y][num] += dfs(x,i,num-1) #dfs
            return dp[x][y][num] % (10**9+7) #结果求模
        res = dfs(0,0,number)
        return res


        # pizza = forest
        # k = number
        # dp_apple = preSum
        #appple = tree
        #'A' = 2
