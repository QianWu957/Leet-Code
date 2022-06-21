class Solution:
    def searchRange(self, nums, target: int):
        res = []
        if not nums: return [-1, -1]
        l, r = 0, len(nums)-1
        ## 寻找左边界
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                if m == 0 or nums[m-1] != target:
                    res.append(m)
                    break
                else:
                    r = m -1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r - l) // 2
            if nums[m] == target:
                if m == len(nums)-1 or nums[m+1] != target:
                    res.append(m)
                    break
                else:
                    l = m +1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return res if res else [-1,-1]

if __name__ == '__main__':
    a = Solution()
    n = [5,7,7,8,8,10]
    tar = 8
    print(a.searchRange(n,tar))
