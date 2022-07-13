class Solution:
    def arrayNesting(self, nums) -> int:
        res = 0
        hashmap = set()
        
        for i in range (len(nums)):
            if nums[i] in hashmap:
                continue

            counter = 1 # Since there is a number to start with, the counter is 1
            index = i
            while nums[index] != i:
                hashmap.add(nums[index])
                index = nums[index] #The value of the current number passes to the index of the next number
                # nums[index] = i
                counter+=1
            hashmap.add(nums[index]) # Although it has jumped out of the while loop, it is still in the for loop. Adding the number under the current pointer to the hashmap can further reduce some for loops

            # hashmap.add(nums[i])
            # print(hashmap)
            res = max (counter, res)
        return res

if __name__ == '__main__':
    a = Solution()
    n = [5,4,0,3,1,6,2]
    print(a.arrayNesting(n))




