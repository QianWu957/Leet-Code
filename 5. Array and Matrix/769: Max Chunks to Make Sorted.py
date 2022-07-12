class Solution:
    def maxChunksToSorted(self, arr) -> int:
        max_ = 0
        counter = 0
        for i, n in enumerate(arr):
            if n > max_: max_ = n
            if i == max_: # check if (k+1)th number equals to k, if yes, that counts as 1 chunk
                counter +=1
        return counter


if __name__ == '__main__':
    a = Solution()
    n = [4,3,2,1,0]
    print(a.maxChunksToSorted(n))
                

            