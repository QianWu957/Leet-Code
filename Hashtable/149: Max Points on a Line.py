class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        res = 2

        for i in range (len(points)):
            hashmap = {}
            x1, y1 = points[i][0], points[i][1]
            for j in range (i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2:
                    a,b,c = 1, 0, -x1
                elif y1 == y2:
                    a,b,c = 0, 1, -y1
                else:
                    a = 1.0
                    b = 1.0 * (x1-x2) / (y2-y1)
                    c = 1.0 * (x1 * y2 -x2 * y1 ) /(y1 - y2)
                if (a,b,c) in hashmap:
                    hashmap[(a,b,c)] +=1
                    res = max(res,hashmap[(a,b,c)])
                else:
                    hashmap [(a,b,c)] =2
        return res        
                
if __name__ == '__main__':
    a = Solution()
    n = [[1,1],[2,2],[3,3]]
    print(a.maxPoints(n))