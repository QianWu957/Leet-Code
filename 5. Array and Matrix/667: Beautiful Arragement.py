class Solution:
    def constructArray(self, n: int, k: int):
        res = []
        for i in range(1, n-k):
            res.append(i)
        # print(res)

        j = 0
        for i in range(n-k, n+1):
            res.append(i)
            res.append(n-j)
            j+=1
        return res[:n]

if __name__ == '__main__':
    a = Solution()
    n = 8
    k = 4
    print(a.constructArray(n,k))