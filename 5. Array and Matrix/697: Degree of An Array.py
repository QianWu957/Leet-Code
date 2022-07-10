class Solution:
    def findShortestSubArray(self, nums) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [1,i,i]

            else:
                hashmap[nums[i]][0]+=1
                hashmap[nums[i]][2]=i
        print(hashmap)

        freq = []
        for v in hashmap.values():
            freq.append(v[0])
        print(freq)

        degree = max(freq)

        print(degree)
        min_ = len(nums)
        for key, val in hashmap.items():
            if val[0] == degree: #make sure this val shows up most of the times
                min_ = min(min_ , val[2]-val[1]+1)
        return min_

if __name__ == '__main__':
    a = Solution()
    n = [1,2,2,3,1]
    print(a.findShortestSubArray(n))




            

