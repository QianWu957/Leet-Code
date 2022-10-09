class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        timeMax = logs[0][1]
        res = logs[0][0]
        for i in range(1,len(logs)):
            if logs[i][1] - logs[i-1][1] > timeMax:
                timeMax = logs[i][1] - logs[i-1][1]
                res = logs[i][0]
            elif logs[i][1] - logs[i-1][1] == timeMax:
                res = min(logs[i][0],res)
        return res

