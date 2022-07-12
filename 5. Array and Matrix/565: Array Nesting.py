class Solution:
    def arrayNesting(self, nums) -> int:
        # n= len(nums)
        # seen = [False] * n
        # # print(seen)
        # ans=0
        # for num in nums:
        #     print(seen[num])
        #     l =0
        #     while not seen[num]:
        #         seen[num] = True
        #         # print(seen[num])
        #         l+=1
        #         num = nums[num]
        #     ans = max(ans,l)
        # return ans

        res = 0
        hashset = set()
        for i in range(len(nums)):
            if nums[i] in hashset:
                continue
            temp = 1
            index = i
            while nums[index] != i:
                hashset.add(nums[index])
                index = nums[index]
                temp += 1
            hashset.add(nums[i])
            res = max(temp, res)
        return res
     
if __name__ == '__main__':
    a = Solution()
    n = [5,4,0,3,1,6,2]
    print(a.arrayNesting(n))



