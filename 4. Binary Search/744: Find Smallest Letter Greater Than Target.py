class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        # if not letters: return 0

        # if target >= letters[-1]:
            
        l , r = 0 , len(letters)-1
        while l <= r:
            mid = l+(r-l)//2
            if target >= letters[mid] :
                l = mid +1
            elif target < letters[mid]:
                r = mid -1
        print(l)
        if l < len(letters):
            return letters[l]
        else:
            return letters[0]

if __name__ == '__main__':
    a = Solution()   
    
    input = ["c","f","j"]
    target = "c"
    print(a.nextGreatestLetter(input,target))


        # l , r = 0 , len(letters)-1
        # while l <= r:
        #     mid = l+(r-l)//2
        #     if target >= letters[mid]:
        #         l = mid+1
        #     elif target < letters[mid]:
        #         r =mid-1

        # if l < len(letters):
        #     return letters[l]
        # else:
        #     return letters[0]