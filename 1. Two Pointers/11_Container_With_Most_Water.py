class Solution:
    def maxArea(self, height) :
        if len(height) < 2: return []

    
        head, tail = 0, len(height)-1
        new_area = 0
        while head < tail:
            area = (tail - head) * min(height[head], height[tail])
            new_area = max(area, new_area)
            
            if height[head] < height[tail]:
                head +=1
            else:
                tail -=1
        return new_area

if __name__ == "__main__":
    a = Solution()
    height = [33,67,90,4,14,562,6,9,16,33,88,2,9,10,79]
    s = 5
    print(a.maxArea(height))