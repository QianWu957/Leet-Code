class Solution:
    def containsDuplicate(self, nums) -> bool:
        if not nums: return False
        if len(nums) < 2: return False
        hashset = set()
        for val in nums:
            if val in hashset:
                return True
            else:
                hashset.add(val)
        return False


if __name__ == '__main__':
    a = Solution()
    n = [1,2,3,1]
    print(a.containsDuplicate(n))

        
    
     
        
       
        