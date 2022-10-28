class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
    
        prediff = nums[1] - nums[0]
        cur_len = (2 if prediff != 0 else 1)

        for i in range(2,len(nums)):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prediff <= 0) or (diff < 0 and prediff >= 0):
                cur_len +=1
                prediff = diff
            
        return cur_len



        # if not nums: return []
        # dp_up = [1] * len(nums)
        # dp_down = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp_up[i] = max(dp_up[i], dp_down[j] +1 )
                
        #         elif nums[i] < nums[j]:
        #             dp_down[i] = max(dp_down[i], dp_up[j] +1 )

        # return max(max(dp_down), max(dp_up))



