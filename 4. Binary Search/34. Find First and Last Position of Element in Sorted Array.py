class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # flag = 0
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] == target and flag == 0:
        #         res.append(i)
        #         res.append(i)
        #         flag =1
        #     elif nums[i]== target:
        #         # res.append(i-1)
        #         res[-1] = i

        # if len(res)>=1:
        #     return res
        # else:
        #     return [-1,-1]
        if not nums: return [-1,-1]
        res = []
        l, r = 0 , len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    res.append(mid)
                    break
                else:
                    r = mid -1

            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid +1
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid+1]!= target:
                    res.append(mid)
                    break
                else:
                    l = mid +1
            elif nums[mid]> target:
                r = mid -1
            else:
                l = mid+1
        print(res)
        print(len(res))

        if len(res) >= 1:
            return res
        else:
            return [-1,-1]

if __name__ == '__main__':
    a = Solution()
    n = [5,7,7,8,8,10]
    tar = 8
    print(a.searchRange(n,tar))
