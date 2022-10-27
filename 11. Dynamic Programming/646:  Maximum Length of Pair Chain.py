class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Greedy
        pairs = sorted(pairs, key = lambda x:(x[1],x[0]))

        print(pairs)

        pre = pairs[0][1]
        res = 1
        for i in range(1,len(pairs)):
            if pairs[i][0] > pre:
                res +=1
                pre= pairs[i][1]
        return res

        # Dynamic Programming
        # pairs.sort()
        # print(pairs)

        # dp = [1] * len(pairs)

        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[j][1] < pairs[i][0]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)
