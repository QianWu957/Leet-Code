class Solution:
    def dailyTemperatures(self, temperatures):
        if not temperatures: return []
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                tem = stack.pop()
                res[tem[1]] = i - tem[1] 
            stack.append((temperatures[i],i))
        return res

if __name__ == '__main__':
    a = Solution()
    t = [73,74,75,71,69,72,76,73]   
    print(a.dailyTemperatures(t))
        


