class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
  
        intervals.sort(key = lambda x:(x[1],x[0]))

        res = 1
        pre = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0] >= pre:
                res+=1
                pre = intervals[i][1]
        return len(intervals)-res